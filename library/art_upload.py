from ansible.module_utils.basic import AnsibleModule
import requests
import urllib3
import json
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
def main():
  module = AnsibleModule(
  argument_spec = dict(
    src_file = dict(required=True, type=str),
    arti_file = dict(default='artfactory_dir',type=str),
    arti_url = dict(required=True, type=str),
    upload_dir = dict(default='',required=False,type=str),
    user = dict(required=True, type=str),
    password= dict(required=True, type='str', no_log=True),
    validate_certs = dict(default=False,type='bool'),
    upload_name = dict(required=True, type=str)
  )
  )
  
  result = dict(
    changed=False,
    original_message='',
    message=''
  )
  
  src_file = str(module.params['src_file'])
  validate_certs = bool(module.params['validate_certs'])
  
  files = {'file': open(src_file,'rb')}
  
  base_url = 'http://'
  headers = {'Content-type': 'application/binary', 'Accept': 'text/plain'}
  if upload_dir != '':
    url = '{}/{}/{}.format(base_url,upload_dir,upload_name)'
    
  auth = requests.auth.HTTPBasicAuth(user,password)
  try:
    response = requests.put(url=url,auth=auth,verify=validate_certs,files=files,headers=headers)
    module.exit_json(changed=True)    
  except Exception as e:
    module.fail_json(msg="unable to upload file - {}".format(e))
  if response.status_code !=201:
    module.fail_json(msg="unable to upload file. received error code{} with message{}".format(response.status_code,response.text))
  else:
    arti_response = {}
    arti_response['return_code'] = response.status_code
    arti_response['msg'] = response.text
    module.exit_json(changed=True,msg=arti_response)
  
if __name__ == '__main__':
    main()
  
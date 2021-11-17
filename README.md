# Auto Extract Network Devices Monitoring Report to HTML
## Scope: Several network brands and in different zone.


 This Project is Checking F5, Checkpoint, Juniper, Cisco,NetScaler devices health status and formatting output as HTML upload to JFrog Artifactory. auto-send email reports to team members daily. Build CI/CD pipeline in AWX with Bitbucket,rapidly respond the change of requirement. make network engineer relax in daily jobs.
 
## Tool-box server(AWX) 
- CI/CD tool platform: AWX (Ansible tower)
- tools: Ansible. tmsh, bash command line
- Data format: XML, Yaml, HTML.
- Repo: Github
- Target Devices: F5 Checkpoint Juniper Cisco Router and Switch.
- Auth: Service Account, ansible vault encrypt the passwords and username.

## Repo Structure
- main.yml: entry of ansible playbook, create log file for everytime runing, call role **execute** to 
run network device commands, after save all report in log file, call role**create_html** and **push_artifactory**.
- roles: there are roles and tasks in this directory 
- library: there is upload artifactory module code.

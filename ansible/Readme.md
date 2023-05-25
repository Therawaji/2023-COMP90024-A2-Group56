# Ansible Instruction
Group56 Team members:

ZIyi Wang (Student ID: 1166087)\
Zhou Zhou (Student ID: 1234764)\
Xiangyi He (Student ID: 1166146)\
Boyu Pan (Student ID: 1319288)\
Huating Ji (Student ID: 1078362)

**Please note that the instructions below are based on MacOS systems, Windows and Linux systems may differ slightly.
## Vedio Demostration
https://youtu.be/zUpNJwxNqi4

## 1. Installing Ansible and Openstack

```bash
pip install ansible
pip install python-openstackclient
```
## 2. Adding read and write permissions to a file

```bash
chmod u+x launch_mrc_command.sh
chmod u+x install_environments.sh
chmod u+x start_backend.sh
chmod u+x deploy_web.sh
```
## 3. Adding a secret key pair
```bashRun the script
eval `ssh-agent -s`
ssh-add /keys/group56_key.pem
```
## 4. Copy password
```bash
YmM0NDk3YjQ4MzVkNjgy
```
## 5. Run the script
```bash
./launch_mrc_command.sh
./install_environments.sh
./start_backend.sh
./deploy_web.sh
```

# Ansible Instruction

**注意：**以下说明基于 MacOS 系统，Windows 和 Linux 系统可能会有些许不同。
## Vedio Demostration
https://youtu.be/zUpNJwxNqi4

## 1. 安装 Ansible 和 Openstack

在您的本地计算机上运行以下命令以安装 Ansible 和 Openstack：

```bash
pip install ansible
pip install python-openstackclient
```
## 2. 为文件添加读写权限
执行以下命令给脚本添加执行权限：

```bash
chmod u+x launch_mrc_command.sh
chmod u+x install_environments.sh
chmod u+x start_backend.sh
chmod u+x deploy_web.sh
```
## 3. 添加秘钥对
```bash
执行以下命令以添加秘钥对：
eval `ssh-agent -s`
ssh-add /keys/group56_key.pem
```
## 4. 复制密码
```bash
YmM0NDk3YjQ4MzVkNjgy
```
## 5. 运行脚本
```bash
./launch_mrc_command.sh
./install_environments.sh
./start_backend.sh
./deploy_web.sh
```
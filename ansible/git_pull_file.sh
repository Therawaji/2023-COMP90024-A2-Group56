#!/bin/bash
export ANSIBLE_HOST_KEY_CHECKING=False
. ./unimelb-comp90024-2023-grp-56-openrc.sh; ansible-playbook --ask-become-pass git_pull_file.yaml -i inventory/hosts.ini
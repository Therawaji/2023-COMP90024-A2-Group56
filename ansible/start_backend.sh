#!/bin/bash

export ANSIBLE_HOST_KEY_CHECKING=False
. ./unimelb-comp90024-2023-grp-56-openrc.sh; ansible-playbook --ask-become-pass start_backend.yaml -i inventory/hosts.ini
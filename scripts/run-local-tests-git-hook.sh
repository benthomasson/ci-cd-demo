#!/bin/bash  -ex
source ~/venv/ansible-events/bin/activate
ansible-events --rules git-hook-test-rules.yml -i inventory.yml -S sources ${1} --vars local-vars.yml

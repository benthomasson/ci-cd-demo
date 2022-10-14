#!/bin/bash  -ex
source ~/venv/ansible-rulebook/bin/activate
export ANSIBLE_FORCE_COLOR=true
ansible-rulebook --rulebook local-test-rules.yml -i inventory.yml -S sources ${1} --vars local-vars.yml

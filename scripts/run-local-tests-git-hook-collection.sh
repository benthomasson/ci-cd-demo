#!/bin/bash  -ex
source ~/venv/ansible-events/bin/activate
ansible-events --rules benthomasson.eda.git-hook-test-rules -i inventory.yml --vars local-vars.yml

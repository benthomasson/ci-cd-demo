#!/bin/bash  -ex
source ~/venv/ansible-events/bin/activate
ansible-events --rules benthomasson.eda.local-test-rules -i inventory.yml --vars local-vars.yml

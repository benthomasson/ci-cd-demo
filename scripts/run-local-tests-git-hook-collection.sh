#!/bin/bash  -ex
source ~/venv/ansible-rulebook/bin/activate
ansible-rulebook --rulebook benthomasson.eda.git-hook-test-rules -i inventory.yml --vars local-vars.yml

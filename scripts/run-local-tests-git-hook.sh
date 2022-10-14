#!/bin/bash  -ex
source ~/venv/ansible-rulebook/bin/activate
ansible-rulebook --rulebook git-hook-test-rules.yml -i inventory.yml -S sources ${1} --vars local-vars.yml

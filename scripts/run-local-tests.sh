#!/bin/bash  -ex
ansible-events local-test-rules.yml -i inventory.yml -S sources ${1} --vars local-vars.yml

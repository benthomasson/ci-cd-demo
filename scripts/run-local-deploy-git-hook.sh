#!/bin/bash  -ex
ansible-rulebook --rulebook git-hook-deploy-rules.yml -i inventory.yml -S sources ${1} --vars local-vars.yml

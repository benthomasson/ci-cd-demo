#!/bin/bash  -ex
env $(cat env2 | xargs) ./scripts/sendit.sh
env $(cat env2 | xargs) ansible-events ci-cd-rules.yml -i inventory.yml -S sources --env-vars webhook,connection_str,token,queue_name --debug

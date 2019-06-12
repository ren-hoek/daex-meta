#!/usr/bin/env python3
import sys
from pyport import swarm as sw

token = sw.generate_token('admin', 'password')
swarm_id = sw.get_swarm_id(token)

stacks = sw.list_stacks(token)
stack_id = str(list(map(lambda x: x['Id'], filter(lambda x: x['Name'] == sys.argv[1], stacks)))[0])
remove = sw.remove_stack(stack_id, token)
deploy = sw.deploy_stack(
    swarm_id,
    token,
    sys.argv[1],
    sys.argv[2]
)

print(deploy.text)

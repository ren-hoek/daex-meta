#!/usr/bin/env python3
import sys
from pyport import swarm as sw


token = sw.generate_token('admin', 'password')
swarm_id = sw.get_swarm_id(token)

deploy = sw.deploy_stack(
    swarm_id,
    token,
    sys.argv[1],
    sys.argv[2]
)

print(deploy.text)


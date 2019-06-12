#!/usr/bin/env python3
import sys
from pyport import swarm as sw

def get_service_value(v, s, c):
    return list(map(lambda x: x[v], filter(lambda x: x['service_name'] == s, c)))[0]

token = sw.generate_token('admin', 'password')

service_up = False
while not service_up:
    try:
        containers = sw.get_container_summary(sw.list_containers(token))
        cont_id = get_service_value('id', sys.argv[1]	, containers)
        node_name = get_service_value('node_name', sys.argv[1], containers)
        service_up = True
    except:
        service_up = False

add = sw.add_to_container(
    cont_id,
	node_name,
	token,
    sys.argv[2],
	sys.argv[3]
)

sw.print_api_output(add)


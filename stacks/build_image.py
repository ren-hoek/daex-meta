#!/usr/bin/env python3
import sys
from pyport import swarm as sw


token = sw.generate_token('admin', 'password')
params = {'t': sys.argv[1]}

image = sw.build_image(
    'feynman',
    token,
    params,
    sys.argv[2]
)

sw.print_api_output(image)


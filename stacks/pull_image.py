#!/usr/bin/env python3
import sys
from pyport import swarm as sw


token = sw.generate_token('admin', 'password')
pull = sw.pull_image(
    sys.argv[1],
    token
)

print(pull.text)


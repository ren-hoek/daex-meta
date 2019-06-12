#!/usr/bin/env python3
import sys
from pyport import swarm as sw

def drop_blank_tags(i):
    return list(filter(lambda x: x['RepoTags'] != None, i))

token = sw.generate_token('admin', 'password')

images = drop_blank_tags(sw.list_images(token))

img_id = list(map(lambda x: x['Id'], filter(lambda x: sys.argv[1] in x['RepoTags'], images)))[0]

tag = sw.tag_image(
    token,
    img_id,
    sys.argv[2]
)

print(tag.text)

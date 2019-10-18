#!/bin/bash
docker node update --label-add gitlab=true feynman
docker node update --label-add redis=true faraday
docker node update --label-add mongo=true faraday
docker node update --label-add nginx=true faraday
docker node update --label-add daex=true feynman
docker node update --label-add registry=true feynman
docker node update --label-add jenkins=true dirac


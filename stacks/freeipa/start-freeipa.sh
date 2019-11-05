docker run --rm --name freeipa \
   --sysctl net.ipv6.conf.all.disable_ipv6=0 \
   --network docproc2 \
   --network-alias ipa.daex.lan \
   -p 80:80 -p 443:443 -p 389:389 -p 636:636 -p 88:88 -p 464:464 \
   -p 88:88/udp -p 464:464/udp -p 123:123/udp \
   -ti \
   -h ipa.daex.lan \
   -v /sys/fs/cgroup:/sys/fs/cgroup:ro \
   --tmpfs /run --tmpfs /tmp \
   -v ipa-data:/data:Z freeipa-server


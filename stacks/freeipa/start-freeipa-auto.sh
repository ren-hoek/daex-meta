docker run --rm --name freeipa \
   --sysctl net.ipv6.conf.all.disable_ipv6=0 \
   --network docproc2 \
   --network-alias ipa.daex.lan \
   -d \
   -h ipa.daex.lan \
   -v /sys/fs/cgroup:/sys/fs/cgroup:ro \
   --tmpfs /run --tmpfs /tmp \
   -v ipa-data:/data:Z docker.service:5000/daex-meta/freeipa:latest


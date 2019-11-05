docker run --rm --name ldap \
   --network docproc2 \
   -p 8787:8787 \
   -v /sys/fs/cgroup:/sys/fs/cgroup:ro \
   -v /tmp/$(mktemp -d):/run \
   -v ldap_home:/home \
   -d docker.service:5000/daex-meta/ldap


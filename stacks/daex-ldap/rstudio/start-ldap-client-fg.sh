docker run --rm --name ldap \
   --network docproc2 \
   -p 8787:8787 \
   -v /sys/fs/cgroup:/sys/fs/cgroup:ro \
   --mount type=tmpfs,destination=/run \
   -v ldap_home:/home \
   -it docker.service:5000/daex-meta/ldap


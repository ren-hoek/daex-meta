docker run --rm --name jupyter_ldap \
   --network docproc2 \
   -p 8088:8000 \
   -v ldap_home:/home \
   -v /sys/fs/cgroup:/sys/fs/cgroup:ro \
   --mount type=tmpfs,destination=/run \
   -it docker.service:5000/daex-meta/jupyterhub:ldap


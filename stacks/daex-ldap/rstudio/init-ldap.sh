#!/bin/bash
authconfig --enableldap --enableldapauth --ldapserver=ipa.daex.lan --ldapbasedn="dc=daex,dc=lan" --enablemkhomedir --update
authconfig --enableldaptls --update
while true; do sleep 100; done


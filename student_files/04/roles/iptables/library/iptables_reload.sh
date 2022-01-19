#!/bin/bash

JSON_FMT='{
  "changed": false,
  "msg": "Reloading iptables because of changed configuration file"
}'

/usr/sbin/iptables-restore /etc/sysconfig/iptables
printf %s "$JSON_FMT"
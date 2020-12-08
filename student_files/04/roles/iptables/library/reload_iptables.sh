#!/bin/bash

JSON_FMT='{
  "changed": false,
  "msg": "Reload iptables via Bash command after config file change)",
  "date": "%s"
}'

/usr/sbin/iptables-restore /etc/sysconfig/iptables
printf "$JSON_FMT" "$(date)"


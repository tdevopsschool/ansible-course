#!/bin/bash
#iptables-restore /etc/sysconfig/iptables
JSON_FMT='{
  "changed": true,
  "msg": "Result was $?",
  "date": "%s"
}'

printf "$JSON_FMT" "$(date)"


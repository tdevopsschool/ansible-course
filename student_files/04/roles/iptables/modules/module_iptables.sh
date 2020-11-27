#!/bin/bash
#ip6tables-restore /etc/sysconfig/ip6tables
JSON_FMT='{
  "changed": true,
  "msg": "Result was $?",
  "date": "%s"
}'

printf "$JSON_FMT" "$(date)"


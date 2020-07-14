#!/bin/bash

if iptables-restore /etc/sysconfig/iptables; then
    JSON='{ "changed": true, "msg": "iptables is reloaded", "date": "%s" }'
else
    JSON='{ "changed": false, "msg": "iptables is not reloaded", "date": "%s" }'
fi

printf "$JSON" "$(date)"

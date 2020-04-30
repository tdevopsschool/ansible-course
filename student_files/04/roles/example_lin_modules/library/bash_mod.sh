#!/bin/bash

JSON_FMT='{
  "changed": false,
  "msg": "Hello, World! (in Bash)",
  "date": "%s"
}'

printf "$JSON_FMT" "$(date)"


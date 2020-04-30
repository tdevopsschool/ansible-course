#!/bin/bash

ansible localhost -m setup
ansible localhost -m yum -a "name=httpd,git state=present"
ansible localhost -m git -a "repo=https://github.com/ultral/2048.git dest=/var/www/html force=true"
ansible localhost -m iptables -a "chain=INPUT protocol=tcp destination_port=80 ctstate=NEW jump=ACCEPT"
ansible localhost -m systemd -a "name=httpd state=started"

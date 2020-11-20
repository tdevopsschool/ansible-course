#!/bin/bash

yum -y install httpd iptables-services git
git clone https://github.com/ultral/2048.git /var/www/html
iptables -A INPUT -m tcp -p tcp --dport 80 -j ACCEPT
systemctl start httpd

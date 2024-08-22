#!/bin/bash
nohup ./chain-report-server >> server.log 2>&1 &
mkdir -p /etc/nginx/conf.d/
mv chainnode.conf /etc/nginx/conf.d/
sed -i "s:include /etc/nginx/sites-enabled:#include /etc/nginx/sites-enabled:g" /etc/nginx/nginx.conf
nginx -g 'daemon off;'
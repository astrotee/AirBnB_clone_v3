#!/usr/bin/env bash
# set up web servers

if [ ! -x /usr/sbin/nginx ]; then
    apt update
    apt install nginx -y
fi

mkdir -p /data/web_static/releases/test/
mkdir -p /data/web_static/shared/

if [ -L /data/web_static/current ]; then
    rm -f /data/web_static/current
fi
ln -s /data/web_static/releases/test /data/web_static/current

echo "It's working!" > /data/web_static/releases/test/index.html

chown -R ubuntu:ubuntu /data/

hbnb_static="\tlocation /hbnb_static {\n\t\talias /data/web_static/current/;\n\t\tautoindex off;\n\t}\n"
if ! grep -q 'location /hbnb_static' /etc/nginx/sites-enabled/default; then
    sed -i s'|^}|'"${hbnb_static}"'}|' /etc/nginx/sites-enabled/default
fi

service nginx reload

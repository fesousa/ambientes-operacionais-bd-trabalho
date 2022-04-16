#!/bin/bash
yum update -y
amazon-linux-extras install epel -y
yum install nginx -y
yum install git -y
yum install gcc -y
yum install build-essential -y
yum install python3-pip python3-devel python3-setuptools libpq-dev -y
mkdir /var/www
cd /var/www
git clone https://github.com/fesousa/ambientes-operacionais-bd-trabalho.git /var/www
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
cp /var/www/app.service /etc/systemd/system
chmod -R 755 /var/www
chown -R ec2-user:nginx /var/www
mkdir /var/log/uwsgi
chown ec2-user:nginx /var/log/uwsgi/
systemctl start app
systemctl enable app
mv /etc/nginx/nginx.conf /etc/nginx/nginx.conf-orig
cp nginx.conf /etc/nginx/nginx.conf
cp app.conf /etc/nginx/conf.d/app.conf
systemctl start nginx
systemctl enable nginx
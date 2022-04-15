#!/bin/bash
yum update -y
yum install python3-pip python-dev nginx -y
yum install git -y
pip3 install virtualenv

mkdir /home/ec2-user/app
cd /home/ec2-user/app
git clone https://github.com/fesousa/ambientes-operacionais-bd-trabalho.git /home/ec2-user/app

virtualenv venv
source ./venv/bin/activate
pip3 install gunicorn flask
cp app.conf /etc/init/myproject.conf
#!/bin/bash
yum update -y
yum install python-pip python-dev nginx -y
amazon-linux-extras install nginx1 -y
yum install git -y
pip install virtualenv

mkdir /home/ec2-user/app
cd /home/ec2-user/app
git clone https://github.com/fesousa/ambientes-operacionais-bd-trabalho.git /home/ec2-user/app

virtualenv venv
source ./venv/bin/activate
pip install gunicorn flask
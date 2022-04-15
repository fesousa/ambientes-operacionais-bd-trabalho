#!/bin/bash
yum update -y

pip3 install virtualenv
mkdir /home/ec2-user/repo
cd /home/ec2-user/repo
git clone https://github.com/fesousa/ambientes-operacionais-bd-trabalho.git /home/ec2-user/repo
cd /home/ec2-user/repo

virtualenv venv
source venv/bin/activate

pip3 install flask gunicorn

cp /home/ec2-user/repo/app.service /etc/systemd/system/app.service

amazon-linux-extras install nginx1 -y


yum install python3-pip python-dev nginx -y
yum install git -y
pip3 install virtualenv

mkdir /home/ec2-user/repo
cd /home/ec2-user/repo
git clone https://github.com/fesousa/ambientes-operacionais-bd-trabalho.git /home/ec2-user/repo
cd /home/ec2-user/repo/app

virtualenv venv
source ./venv/bin/activate
pip3 install gunicorn flask
mkdir /etc/init
cp /home/ec2-user/repo/app.conf /etc/init/app.conf
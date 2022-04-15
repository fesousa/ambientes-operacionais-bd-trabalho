#!/bin/bash
yum update -y
amazon-linux-extras install epel -y
yum install nginx -y
yum install git -y
yum install gcc -y
yum install build-essential -y
yum install python3-pip python3-devel python3-setuptools -y
mkdir /var/www
cd /var/www
git clone https://github.com/fesousa/ambientes-operacionais-bd-trabalho.git /var/www

python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
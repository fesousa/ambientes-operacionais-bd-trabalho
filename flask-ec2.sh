#!/bin/bash
yum update -y
yum install python3-venv -y
yum install git -y
cd /home/ec2-user
su ec2-user -c "git clone https://github.com/fesousa/ambientes-operacionais-bd-trabalho.git"
cd ambientes-operacionais-bd-trabalho
python3 -m venv venv
source venv/bin/activate
pip install gunicorn flask
cp app.service /etc/systemd/system/app.service
systemctl daemon-reload
systemctl start app
systemctl enable app

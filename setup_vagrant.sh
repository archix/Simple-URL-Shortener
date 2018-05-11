#!/usr/bin/env bash

sudo apt-get -y update
sudo apt-get -y upgrade

sudo apt-get -y install python3-pip python3-venv

# install postgres and setup user and db
sudo apt-get -y install postgresql postgresql-contrib
(cd /home/vagrant/app; sudo -u postgres psql -f fixtures.sql)

(cd /home/vagrant/app; python3 -m venv .env)
(cd /home/vagrant/app; .env/bin/pip install --upgrade pip)
(cd /home/vagrant/app; .env/bin/pip install -r requirements.txt)
(cd /home/vagrant/app; .env/bin/flask db upgrade)
#!/bin/sh
rm /home/dequr -R
cd /home
git clone git@github.com:edwardmspc/dequr.git
sudo supervisorctl restart dequr
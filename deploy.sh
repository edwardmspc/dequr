#!/bin/sh
cd /home
rm dequr -R
mkdir dequr
cd /dequr
git init
git clone git@github.com:edwardmspc/dequr.git
sudo supervisorctl restart dequr
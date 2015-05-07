#!/bin/sh
rm -r /home/dequr/webapps/dequr/dequr 
cd /home/dequr/webapps/dequr
git clone https://github.com/edwardmspc/dequr.git
./apache2/bin/restart
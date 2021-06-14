#!/bin/bash

clear
path="./agent/barometer/3rd_party/collectd-ves-app/ves_app/"

cat /dev/null > ves_app.log
echo "Make Sure VES Agent script is running before stating VES Agent script."
echo "VES Agent script is running. To stop press CTRL C"
echo "================================================="


python3 $path/ves_app.py --events-schema=$path/host.yaml --loglevel DEBUG --config=$path/ves_app_config.conf

#!/bin/bash
infuxdb_host=127.0.0.1
influxdb_port=3330

#Clear log files before starting collector script
cat /dev/null > /home/ves-dev/ves-dev/monitor.log
cat /dev/null > /home/ves-dev/ves-dev/collector.log

clear
echo  -e "======================================================================================\n"
echo -e "\n"
echo -e "VES-DEV script is started on port 9999, to stop VES-COLLECTOR script press CTRL C \n"
echo -e "\n"
echo  -e "======================================================================================\n"

#Start collector script, service port is 9999

python3 /home/ves-dev/ves-dev/collector/ves/evel-test-collector/code/collector/monitor.py --config /home/ves-dev/ves-dev/collector/ves/evel-test-collector/config/collector.conf --influxdb $infuxdb_host:$influxdb_port --section default > /home/ves-dev/ves-dev/monitor.log 2>&1

#!/bin/bash
echo "Stoping all containers"
sudo killall -9 python2
sudo docker stop $(sudo docker ps -aq)

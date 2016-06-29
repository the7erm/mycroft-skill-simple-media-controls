#!/bin/bash
running=$(ps -Af | grep fmp.py)
if [ "$running" = "" ]
then
    nohup /home/erm/fmp-pg/fmp.py &
    sleep 2
    status = $(wget -qO- http://localhost:5050/status)
    state = $(echo "$status" | awk '{print $1}')
    if [ "$state" != "PAUSED" ]
    then
        wget -qO- 'http://localhost:5050/pause'
    fi
else
    wget -qO- 'http://localhost:5050/pause'
fi

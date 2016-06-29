#!/bin/bash
running=$(ps -Af | grep fmp.py)
if [ "$running" = "" ]
then
    nohup /home/erm/fmp-pg/fmp.py &
else
    status = $(wget -qO- http://localhost:5050/status)
    state = $(echo "$status" | awk '{print $1}')
    if [ "$state" = "PLAYING" ]
    then
        wget -qO- 'http://localhost:5050/next'
    fi
fi
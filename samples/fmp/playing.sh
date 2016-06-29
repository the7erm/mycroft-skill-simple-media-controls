#!/bin/bash
running=$(ps -Af | grep fmp.py)
if [ "$running" = "" ]
then
    nohup /home/erm/fmp-pg/fmp.py &
    sleep 2
fi
status=$(wget -qO- http://localhost:5050/status)
state=$(echo "$status" | awk '{print $1}')
playing=$(echo "$status" | awk '{ s = ""; for (i = 2; i <= NF; i++) s = s $i " "; print s }')
echo "$playing"

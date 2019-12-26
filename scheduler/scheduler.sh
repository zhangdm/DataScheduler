#!/bin/bash

TODAY=${1}



nohup python /data/DataScheduler/scheduler.py  /data/DataScheduler/sql/ex_online_user.sql   ${TODAY} >  /data/DataScheduler/logs/run_${TODAY}.log    2>&1 &

wait



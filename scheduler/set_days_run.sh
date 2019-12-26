#!/bin/bash
BEGIN=${1}
END=${2}

n=$(((`date -d "$END" +%s`-`date -d "$BEGIN" +%s`)/86400))
flag=0
while [ $flag -le $n ]
do
     CHANGE_DAY=`date -d "$BEGIN $flag day" "+%Y%m%d"`
     YEAR=`expr substr ${CHANGE_DAY} 1 4`
     MONTH=`expr substr ${CHANGE_DAY} 5 2`
     DAY=`expr substr ${CHANGE_DAY} 7 2`
     
     

     bash /data/DataScheduler/scheduler.sh  $YEAR-$MONTH-$DAY


     flag=$(( $flag + 1 ))
done

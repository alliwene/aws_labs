#!/bin/bash
name="uthman"

touch "$name-1"
largest=$(ls | sed 's/uthman-//' | sort -n | tail -1)
stop_num=24
stop=$(($largest+$stop_num)) 

for x in $(seq $largest $stop)
do 
	touch "$name-$x"
done

echo "Complete"

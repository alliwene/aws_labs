#!/bin/bash
name="uthman"

counter=2
touch "$name-$counter"
largest=$(ls | sed 's/uthman-//' | sort -n | tail -1) 
while [ $counter -le 25 ]
do 
	touch "$name-$counter"
	((counter++))
done

echo "Complete"
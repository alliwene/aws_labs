#!/bin/bash
echo "What is your name?"
read name
DAY="$(date +%d%m%Y)"
DIR="$name-$DAY"
mkdir $DIR
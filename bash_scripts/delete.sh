#!/bin/bash

if cp -f file1 /tmp
then
rm -f file1
else
echo "No such file."
fi

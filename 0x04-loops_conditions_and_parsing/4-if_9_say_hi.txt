#!/usr/bin/env bash
# Initialize a variable x to 1
x=1
while [ $x -le 10 ]
do
    echo "Best School"
    if [ $x -eq 9 ]
    then
        echo "Hi"
    fi
    x=$((x + 1))
done

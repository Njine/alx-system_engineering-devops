#!/usr/bin/env bash
# Initialize the hour to 0
hour=0
while ((hour <= 12)); do
    echo "Hour: $hour"
    minutes=1
    while [ $minutes -lt 60 ]; do
        echo "$minutes"
        ((minutes++))
    done
    hour=$((hour + 1))
done

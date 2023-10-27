#!/usr/bin/env bash
# Initialize a counter c to 1
luck=1
while ((luck <= 10)); do
    if ((luck == 4)); then
        echo "bad luck"
    elif ((luck == 8)); then
        echo "good luck"
    else
        echo "Best School"
    fi
    luck=$((luck + 1))
done

#!/usr/bin/env bash
# This script is displaying luck.
luck=1
while ((luck <= 20)); do
    echo "$luck"
    case $luck in
	4)
	    echo "bad luck from China"
	    ;;
	9)
	    echo "bad luck from Japan"
	    ;;
	17)
	    echo "bad luck from Italy"
	    ;;
    esac
    luck=$((luck + 1))
done	

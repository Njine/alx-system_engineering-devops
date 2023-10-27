#!/usr/bin/env bash
# This script is displaying username, userid and home directory using read with text
while IFS=: read -r username password userID groupID userINFO home command; do
    echo -n "The user $username is part of the $groupID gang, "
    echo -n "lives in $home and rides $command."
    echo -n " $userID's place is protected by the passcode $password, "
    echo "more info about the user here: $userINFO"
done < "/etc/passwd"

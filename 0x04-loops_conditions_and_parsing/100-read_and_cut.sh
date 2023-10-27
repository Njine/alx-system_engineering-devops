#!/usr/bin/env bash
# This script displays username, userid and home directory using read

while IFS=: read -r username userid home_directory _; do
    echo "Username: $username, User ID: $userid, Home Directory: $home_directory"
done < "/etc/passwd"

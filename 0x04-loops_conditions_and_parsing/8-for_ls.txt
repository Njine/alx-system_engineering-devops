#!/usr/bin/env bash
#Script that lists files
for i in *; do
    echo "${i#*-}"
done

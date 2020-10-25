#!/bin/sh

TIMEOUT ="5s"

while : ; do
    python bot.py
    echo "restarting in $TIMEOUT"
    sleep $TIMEOUT
done
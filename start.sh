#!/bin/sh

TIMEOUT="5s"

while : ; do
    python3 bot.py
    echo "restarting in $TIMEOUT"
    sleep $TIMEOUT
done
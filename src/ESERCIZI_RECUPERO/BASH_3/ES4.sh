#!/bin/bash
echo "Please enter: start, stop or restart"
read variabile
if [ "$variabile" = "start" ]
then
echo "system started"
elif [ "$variabile" = "stop" ]
then
echo "system stopped"
elif [ "$variabile" = "restart" ]
then
echo "system stopped"
echo "system started"
else
echo "wrong command"
fi
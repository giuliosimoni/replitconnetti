#!/bin/bash
declare -i a=43
declare -i b
read b
if [ $b -eq $a ]
then echo "is equal to $a"
elif [ $b -gt $a ]
then echo "is greater than $a"
elif [ $b -lt $a ]
then echo "is less than $a"
fi
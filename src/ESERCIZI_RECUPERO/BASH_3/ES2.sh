#!/bin/bash
clear
echo enter directory name
read dname
if cd $dname
then echo "changed to $dname"
pwd
fi
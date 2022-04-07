#!/bin/bash
read N
num=1
a=10
if [ $N -gt 1 ]
 then
    while [ $num -le $N ];
      do
       echo $num
       num=$[$num+1]
      done
 else
 echo $a
 fi
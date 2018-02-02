#!/bin/sh
c=$#
echo "the arguments in the reverse order :"
while [ $c -ne 0 ]
do
eval echo \$$c
c=`expr $c - 1`
done

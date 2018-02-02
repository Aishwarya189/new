#!/bin/sh
perm1=`ls -l $1 |cut -c 1-10`
perm2=`ls -l $2 |cut -c 1-10`
if [ $perm1 = $perm2 ]
 then
   echo "equal and $perm1"
else  
   echo "not equal"
   echo "$perm1"
   echo "$perm2"
fi


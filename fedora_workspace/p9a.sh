#!/bin/sh
for i
do 
echo "echo the file $i created"
echo "cat>$i <<'END'"
cat $i
echo "END"
done

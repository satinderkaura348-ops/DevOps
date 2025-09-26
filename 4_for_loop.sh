#!/bin/bash
#
#
read -p "Enter a number below 10: " num

for (( num=num; num<=10 ; num++ ));
do
	echo "$num"
done

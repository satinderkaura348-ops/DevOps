#!/bin/bash


function usage() {
	echo
	echo "Usage:  This script allows creation of 5 new users."
	echo
	echo "How:    Enter user name that you wish to create."
}

if [[ $1 == "-help" ]]; 
then
	usage
fi



function create_new_user() {
	read -p "Enter the username you wish to create: " username
	if id "$username"&>/dev/null;
	then
	echo "$username user already exists!"
		exit 1
	elif getent group | grep -qi "$username"
	then
		echo "$username user already belong to group $( getent group | grep -i "$username" |  awk -F: '{print $1}')"
		exit 1
	else
		useradd "$username"
	fi
}

for (( i=1; i<=5; i++ ));
do 	
	create_new_user
done

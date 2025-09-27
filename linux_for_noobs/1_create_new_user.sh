#!/bin/bash

<<comment
This script creates a new user by asking username and also password
comment

usage() {
	echo "Usage: $0"
	echo "This script creates a new Linux user"
	echo "You will be prompted to enter: "
	echo "- Username"
	echo "- Password(entered twice)"
	exit 1
}

if [[ $1 == "-help" ]]; then
	usage
fi


read -p "which user would you like to create: " user

# &>/dev/null check for if user already exists
if id "$user" &>/dev/null; then
	echo "User already exist"
	exit 1
elif [[ ! "$user" =~ ^[a-zA-Z0-9_]+$ ]]; then
	echo "Error: Username can only contain letters, numbers and underscores."
	exit 1
elif grep -q "$user" /etc/shadow; then	
	echo "User stale existed in /etc/shadow"
	exit 1
elif getent group | grep -wq "$user"; then
	echo "$user already belong to a group"
	exit 1
else
	useradd "$user"
	echo "User $user has been created"
fi

# -s silently asks for password without reflecting on screen
read -sp "Enter your password: " password1
echo
read -sp "Confirm your password: " password2

if [[ $password1 != $password2 ]]; then
	echo "Passwords do not match"
	exit 1
fi

# chpasswd changes a user's password in a non-interactive way
echo "$user:$password1" | chpasswd
echo
echo "****Password has been successully updated****"

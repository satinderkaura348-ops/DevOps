#!/bin/bash

function create_user() {
	read -p "Enter the username: " user
	useradd $user
	echo "$user has been created"

}
create_user

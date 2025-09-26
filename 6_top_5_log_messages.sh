#!/bin/bash
#
# This script finds the top 5 most common log messages in Linux_2k.log using awk and sort.
#

usage(){
	echo
	echo "This script displays the top 5 most common log messages."
	echo
	echo "Usage: Provide the filename from /var/log as the first argument."
	echo
	echo "Example: To see the top 5 logs from the 'messages' file in /var/log,"
	echo "simply run the script with 'messages' as the argument."

}

if [[ "$1" == "-help" ]];
then
	usage
	exit 1
fi


last_5_common_logs() {
	cat /var/log/$1 | sort | uniq -c | sort -n | tail -5 | awk '{print $5 $6 $8}'
}
last_5_common_logs "$1"

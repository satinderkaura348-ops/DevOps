#!/bin/bash
#



usage() {
    echo "=================================================="
    echo "                 LOG ANALYZER SCRIPT             "
    echo "=================================================="
    echo
    echo "Description:"
    echo "  This script analyzes the latest web server logs"
    echo "  from /var/log/access.log and generates a report"
    echo "  of the 10 most visited URLs along with the"
    echo "  associated client IP addresses and request counts."
    echo
    echo "Usage:"
    echo "  ./8_log_analyzer.sh [options]"
    echo
    echo "Options:"
    echo "  -help    Display this help message and exit."
    echo
    echo "Output:"
    echo "  The script produces a formatted report showing:"
    echo "    - Top 10 URLs by request count"
    echo "    - Each URL's total hits"
    echo "    - List of client IPs with individual request counts"
    echo "=================================================="
}

if [ "$1" = "-help" ]; then
    usage
    exit 0
fi


top_ten_url=$(cat /var/log/access.log | awk '{print $7}' | sort | uniq -c | sort -nr| head -10)

while read -r line;
do 
	count=$(echo "$line" | awk '{print $1}')
	url=$(echo "$line" | awk '{print $2}')

	echo "URL: $url, Hits: $count"
	awk -v u="$url" '$7 == u {print $1}' /var/log/access.log | sort | uniq -c | sort -nr | while read -r ipcount ip; do
		echo " $ip ($ipcount requests)"
	done
	echo "------------------------"
	
done <<< "$top_ten_url"



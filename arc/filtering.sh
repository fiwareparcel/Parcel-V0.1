#!/bin/bash

while true; do
	cut -d ',' -f 1,3,4 1-01.csv > p; ./filter.sh p > filteredmacs.csv
	sleep 5
done

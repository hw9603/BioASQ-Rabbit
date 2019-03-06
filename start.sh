#!/usr/bin/env bash

for dir in Splitter Expander Ranker Tiler Results; do
	echo "Starting $dir"
	cd $dir
	python service.py &
	cd -
done 
echo "Services started"
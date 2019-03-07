#!/usr/bin/env bash

for dir in Splitter Expander Ranker Tiler Results; do
	echo "Starting $dir"
	cd $dir
	python service.py &
	cd -
done
echo "Services started"

#if [ "$RABBIT_HOST" = "" ] ; then
#    RABBIT_HOST=172.17.0.2
#fi
#
#for name in splitter expander ranker tiler results; do
#    docker run -d -e RABBIT_HOST=$RABBIT_HOST --name $name hw9603/$name
#
#done
#
#echo "Services started"
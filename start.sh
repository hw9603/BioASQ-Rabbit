#!/usr/bin/env bash

#for dir in Splitter Expander Ranker Tiler Results; do
#	echo "Starting $dir"
#	cd $dir
#	python service.py &
#	cd -
#done
#echo "Services started"
if [ "$RABBIT_HOST" = "" ] ; then
    RABBIT_HOST=ec2-13-58-28-131.us-east-2.compute.amazonaws.com
fi

for name in splitter expander ranker tiler results; do
    docker run -d -e HOST=$RABBIT_HOST --name $name hw9603/$name

done

echo "Services started"
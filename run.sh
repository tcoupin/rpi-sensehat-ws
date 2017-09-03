#!/bin/bash

if [ -f ~/.mysensehat/pid ]
then
	sudo kill $(cat ~/.mysensehat/pid) && rm ~/.mysensehat/pid
fi

( sudo python ~/.mysensehat/$1 )&

echo $! > ~/.mysensehat/pid
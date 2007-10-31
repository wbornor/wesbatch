#! /bin/bash

SERVER=$1
shift
DIR=$1

if [ -z "$SERVER" ]; then
	echo -ne "usage: sls [user@]host [path]\n"
	exit;
fi

ssh $SERVER "ls $DIR"

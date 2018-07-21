#!/usr/bin/env bash

if [ -e bankapp.db ]
then
    rm bankapp.db
	echo 'Database deleted'
else
    echo 'Database do not exists'
fi

python3 schema.py
echo 'Schema defined'

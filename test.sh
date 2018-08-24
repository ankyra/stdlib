#!/bin/bash

if pip list 2>/dev/null | grep "^nose " > /dev/null ; then
    echo "nose already installed. Nice job. Well smellt."
else
    pip install nose
fi

nosetests -s

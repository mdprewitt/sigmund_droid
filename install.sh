#!/bin/bash

for i in $( cat requirements.txt ) ; do
    pip3 install $i
done

#!/bin/bash

cat $1 | sed 's/\(.\)/\1\n/g' | sort | uniq -c | sort -n

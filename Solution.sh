#!/bin/bash

count=0

for i in {1..1234} 
do
    #Reading o/p.
    output=$(/home/vikasdw/Downloads/qatest-linux-amd64 run)
    
    # Removing whitespace
    output=$(echo "$output" | xargs)
    #incrementing count id maches fizz.
    if [[ "$output" == "fizz" ]]; then
        ((count++))
    fi
done

echo "fizz appear: $count/1234 times." > output.txt

echo "fizz appear: $count/1234 times."

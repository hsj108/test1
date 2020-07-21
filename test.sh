#!/bin/bash

echo "hello"
for i in 1 2 3 4 5
do
    echo "sample_${i}"
    python test1.py ${i}
done

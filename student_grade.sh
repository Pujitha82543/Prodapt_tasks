#!/bin/bash

echo "Enter marks for 5 subjects:"

read -p "Subject 1: " s1
read -p "Subject 2: " s2
read -p "Subject 3: " s3
read -p "Subject 4: " s4
read -p "Subject 5: " s5

total=$((s1+s2+s3+s4+s5))
average=$((total/5))

echo "-----------------"
echo "Total Marks : $total"
echo "Average Marks : $averages"

if [ $average -ge 90 ]; then
    echo "Grade : A"
elif [ $average -ge 75 ]; then
    echo "Grade : B"
elif [$average -ge 60 ]; then
    echo "Grade : C"
elif [$average -ge 50 ]; then
    echo "Grade : D"
else
     echo "Grade : Fail"
fi


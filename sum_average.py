#!/usr/bin/python3

numbers = [int(x) for x in input("Enter list of numbers separated by a space\n").split()]
print("sum = ", sum(numbers))
print("average = ", sum(numbers)/len(numbers))
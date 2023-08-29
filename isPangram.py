#!/usr/bin/python3

def isPangram(str):
    str = str.lower()
    for char in "abcdefghijklmnopqrstuvwxyz":
        if char not in str:
            return False
    return True

string1= "The five boxing wizards jump quickly."

if (isPangram(string1) == True):
    print(string1, "is Pangram")
else :
    print(string1, "is not Pangram")
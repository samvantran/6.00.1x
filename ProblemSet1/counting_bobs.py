'''
Problem Statement:
Write a program that prints the number of times the string 'bob' occurs in s. 

For example, if s = 'azcbobobegghakl', then your program should print
Number of times bob occurs is: 2

Assume s is a string of lower case characters.
'''

s = raw_input()

# counter variable
numBobs = 0

# for every 3 letter string in s, check for match to 'bob'
for i in range(0,len(s)):
    if s[i:i+3] == 'bob':
        numBobs += 1   

print 'Number of times bob occurs is: ', numBobs

    
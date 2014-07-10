'''
Problem statement:
Write a program that counts up the number of vowels contained in the string s. 
Valid vowels are: 'a', 'e', 'i', 'o', and 'u'. 

For example, if s = 'azcbobobegghakl', your program should print:
Number of vowels: 5

Assume s is a string of lower case characters.
'''

s = raw_input()

# counter variable
numVowels = 0

# for every letter in string, check to see if == to vowel
for char in s:
    if char in ('a','e','i','o', 'u'):
        numVowels += 1
        
print 'Number of vowels: ', numVowels
  

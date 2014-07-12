'''
Write a program that prints the longest substring of s in which the letters occur in alphabetical order. 

For example, if s = 'azcbobobegghakl', then your program should print
Longest substring in alphabetical order is: beggh

In the case of ties, print the first substring. For example, if s = 'abcbcd', then your program should print
Longest substring in alphabetical order is: abc

Assume s is a string of lower case characters.
'''

def alpha(s):
    
    # init two strings with first letter of s - to be compared later
    currStr = s[0]
    longest = s[0]
    
    for i in range(1, len(s)):
        # if letter in s >= to the current string, concat letter to curr
        if s[i] >= currStr[-1]:
            currStr += s[i]
            
            # if the current string is bigger, change largest to currStr
            if len(currStr) > len(longest):
                longest = currStr
        else:
            currStr = s[i]
                
    print 'Longest substring in alphabetical order is:', longest


alpha('abcdeasdlknfowipowerabcdefg')

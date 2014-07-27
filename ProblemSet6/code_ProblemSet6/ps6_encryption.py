# 6.00x Problem Set 6
#
# Part 1 - HAIL CAESAR!

import string
import random

WORDLIST_FILENAME = "/Users/svt/Desktop/6.00.1x/ProblemSet6/code_ProblemSet6/words.txt"

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)
def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    inFile = open(WORDLIST_FILENAME, 'r')
    wordList = inFile.read().split()
    print "  ", len(wordList), "words loaded."
    return wordList

def isWord(wordList, word):
    """
    Determines if word is a valid word.

    wordList: list of words in the dictionary.
    word: a possible word.
    returns True if word is in wordList.

    Example:
    >>> isWord(wordList, 'bat') returns
    True
    >>> isWord(wordList, 'asdf') returns
    False
    """
    word = word.lower()
    word = word.strip(" !@#$%^&*()-_+={}[]|\\:;'<>?,./\"")
    return word in wordList

def randomWord(wordList):
    """
    Returns a random word.

    wordList: list of words  
    returns: a word from wordList at random
    """
    return random.choice(wordList)

def randomString(wordList, n):
    """
    Returns a string containing n random words from wordList

    wordList: list of words
    returns: a string of random words separated by spaces.
    """
    return " ".join([randomWord(wordList) for _ in range(n)])

def randomScrambled(wordList, n):
    """
    Generates a test string by generating an n-word random string
    and encrypting it with a sequence of random shifts.

    wordList: list of words
    n: number of random words to generate and scamble
    returns: a scrambled string of n random words

    NOTE:
    This function will ONLY work once you have completed your
    implementation of applyShifts!
    """
    s = randomString(wordList, n) + " "
    shifts = [(i, random.randint(0, 25)) for i in range(len(s)) if s[i-1] == ' ']
    return applyShifts(s, shifts)[:-1]

def getStoryString():
    """
    Returns a story in encrypted text.
    """
    return open("/Users/svt/Desktop/6.00.1x/ProblemSet6/code_ProblemSet6/story.txt", "r").read()


# (end of helper code)
# -----------------------------------


#
# Problem 1: Encryption
#
def buildCoder(shift):
    """
    Returns a dict that can apply a Caesar cipher to a letter.
    The cipher is defined by the shift value. Ignores non-letter characters
    like punctuation, numbers and spaces.

    shift: 0 <= int < 26
    returns: dict
    """
    shifted = {}
    for i in range(26):
        shifted[string.ascii_uppercase[i]] = string.ascii_uppercase[(i + shift) % 26]
        
    for i in range(26):
        shifted[string.ascii_lowercase[i]] = string.ascii_lowercase[(i + shift) % 26]
        
    return shifted
    

def applyCoder(text, coder):
    """
    Applies the coder to the text. Returns the encoded text.

    text: string
    coder: dict with mappings of characters to shifted characters
    returns: text after mapping coder chars to original text
    """
    # create empty string to capture ciphertext
    newString = ''
    
    # load shifted dict
    shift = coder
    
    # for every character in string text, shift by coded amount only if character is an ascii char
    for char in text:
        if char in string.ascii_letters:
            newString += shift[char]
        else:
            newString += char
        
    return newString

def applyShift(text, shift):
    """
    Given a text, returns a new text Caesar shifted by the given shift
    offset. Lower case letters should remain lower case, upper case
    letters should remain upper case, and all other punctuation should
    stay as it is.

    text: string to apply the shift to
    shift: amount to shift the text (0 <= int < 26)
    returns: text after being shifted by specified amount.
    """
    # wrapper function
    return applyCoder(text, buildCoder(shift))

#
# Problem 2: Decryption
#
def findBestShift(wordList, text):
    """
    Finds a shift key that can decrypt the encoded text.

    text: string
    returns: 0 <= int < 26
    """
    
    # initialize counter for most valid words and shift key
    mostValidWords = 0
    bestKey = 0
    
    # applyShift 25 times using different shift keys (e.g. 1, 2, 3... 25)
    for i in range(1, 26):
            
        # create test string to capture shifted text
        testString = applyShift(text, i)
        
        # split test string into a list of individual words
        dividedText = testString.split(' ')
        
        # initialize counter for valid words
        validWords = 0
        
        # check each for word for validity
        for word in dividedText:
            
            # if isWord == True, increment valid word counter
            if isWord(wordList, word):
                validWords += 1
                
        # if current shifted text has more valid words than the last text, 
        # record shift key and reset valid word count
        if validWords > mostValidWords:
            bestKey = i
            mostValidWords = validWords
            validWords = 0
        
    # return shift key that deciphered the most valid words
    print mostValidWords
    return bestKey

def decryptStory():
    """
    Using the methods you created in this problem set,
    decrypt the story given by the function getStoryString().
    Use the functions getStoryString and loadWords to get the
    raw data you need.

    returns: string - story in plain text
    """
    # read file containing encrypted text
    encryptedStory = getStoryString()
    
    # load words
    wordList = loadWords()
    
    # determine best shift key
    bestShift = findBestShift(wordList, encryptedStory)
    
    # return deciphered text
    return applyShift(encryptedStory, bestShift)

#
# Build data structures used for entire session and run encryption
#

if __name__ == '__main__':
    # To test findBestShift:
    wordList = loadWords()
    s = applyShift('Hello, world!', 8)
    bestShift = findBestShift(wordList, s)
    assert applyShift(s, bestShift) == 'Hello, world!'
    # To test decryptStory, comment the above four lines and uncomment this line:
    #    decryptStory()

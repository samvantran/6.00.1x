from ps4a import *
import time


#
#
# Problem #6: Computer chooses a word
#
#
def compChooseWord(hand, wordList, n):
    """
    Given a hand and a wordList, find the word that gives 
    the maximum value score, and return it.

    This word should be calculated by considering all the words
    in the wordList.

    If no words in the wordList can be made from the hand, return None.

    hand: dictionary (string -> int)
    wordList: list (string)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)

    returns: string or None
    """
    
    # Create a new variable to store the maximum score seen so far (initially 0)
    maxScore = 0
    currScore = 0
    
    # Create a new variable to store the best word seen so far (initially None)  
    bestWord = ''
    tempWord = ''
    
    # For each word in the wordList
    for word in wordList:

        # If you can construct the word from your hand
        # copy hand to avoid side effects
        newHand = hand.copy()
        tempWord = ''
    
        # verify word exists and check to see if letters in word match with available letters in hand
        for l in word:
            if newHand.get(l, 0) != 0:
                tempWord += l
                newHand[l] = newHand[l] - 1
            else:
                tempWord = ''
                break
                
        # Find out how much making that word is worth
        if tempWord == '':
            currScore = 0
        else:                
            currScore = getWordScore(tempWord, n)
            # test: print tempWord + ' score: ', currScore
            
            # If the score for that word is higher than your best score
            if currScore > maxScore:

                # Update your best score, and best word accordingly
                maxScore = currScore
                bestWord = tempWord

    # return the best word you found.
    # test: print 'And the best word is: ' + bestWord + ' with a top score of: ', maxScore
    if bestWord == '':
        return 
    else:
        return bestWord

#
# Problem #7: Computer plays a hand
#
def compPlayHand(hand, wordList, n):
    """
    Allows the computer to play the given hand, following the same procedure
    as playHand, except instead of the user choosing a word, the computer 
    chooses it.

    1) The hand is displayed.
    2) The computer chooses a word.
    3) After every valid word: the word and the score for that word is 
    displayed, the remaining letters in the hand are displayed, and the 
    computer chooses another word.
    4)  The sum of the word scores is displayed when the hand finishes.
    5)  The hand finishes when the computer has exhausted its possible
    choices (i.e. compChooseWord returns None).
 
    hand: dictionary (string -> int)
    wordList: list (string)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)
    """
    
    # Keep track of the total score and num of letters
    totalScore = 0
    len = calculateHandlen(hand)
    
    # As long as there are still letters left in the hand:
    while len > 0:
        
        # Display the hand
        print 'Current Hand:', 
        displayHand(hand)
        
        # computer chooses word
        word = compChooseWord(hand, wordList, n)
        
        if word != None:
        # Tell the user how many points the word earned, and the updated total score, in one line followed by a blank line
            wordScore = getWordScore(word, n)
            totalScore += wordScore
            print '"' + word  + '" earned', wordScore, 'points. Total:', totalScore, 'points.'
            print

            # Update the hand 
            hand = updateHand(hand, word)
            len = calculateHandlen(hand)
        else:
            break
                    
    print 'Total score:', totalScore, 
    print 'points.'
    return
    
#
# Problem #8: Playing a game
#
#
def playGame(wordList):
    """
    Allow the user to play an arbitrary number of hands.
 
    1) Asks the user to input 'n' or 'r' or 'e'.
        * If the user inputs 'e', immediately exit the game.
        * If the user inputs anything that's not 'n', 'r', or 'e', keep asking them again.

    2) Asks the user to input a 'u' or a 'c'.
        * If the user inputs anything that's not 'c' or 'u', keep asking them again.

    3) Switch functionality based on the above choices:
        * If the user inputted 'n', play a new (random) hand.
        * Else, if the user inputted 'r', play the last hand again.
      
        * If the user inputted 'u', let the user play the game
          with the selected hand, using playHand.
        * If the user inputted 'c', let the computer play the 
          game with the selected hand, using compPlayHand.

    4) After the computer or user has played the hand, repeat from step 1

    wordList: list (string)
    """
    # init empty hand (dictionary)
    hand = {}
    while True:
        
        # ask for user input
        ans = raw_input('Enter n to play a new hand, r to replay the last hand, or e to end game: ')
        
        # if e, exit
        if ans == 'e':
            return
        
        # if n, deal new hand
        elif ans == 'n':
            hand = dealHand(HAND_SIZE)
            #hand = origHand.copy()
            
            while True:
                # ask user input u or c
                ans2 = raw_input('Enter u to have yourself play, c to have the computer play: ')
                print
                
                # if u, user to play
                if ans2 == 'u':
                    playHand(hand, wordList, HAND_SIZE)
                    break
                    
                # if c, computer to play
                elif ans2 == 'c':
                    compPlayHand(hand, wordList, HAND_SIZE)
                    break
                else:
                    print 'Invalid command.'        
        
        # if r, deal previous hand
        elif ans == 'r':
            
            if hand != {}:
                #hand = origHand.copy()
                
                while True:
                    # ask user input u or c
                    ans2 = raw_input('Enter u to have yourself play, c to have the computer play: ')
                    print
                
                    # if u, user to play
                    if ans2 == 'u':
                        playHand(hand, wordList, HAND_SIZE)
                        break
                        
                    # if c, computer to play
                    elif ans2 == 'c':
                        compPlayHand(hand, wordList, HAND_SIZE)
                        break
                        
                    else:
                        print 'Invalid command.'
                
            else:
                print 'You have not played a hand yet. Please pay a new hand first!'
            
        # else, display invalid response
        else:
            print 'Invalid command.'
        
#
# Build data structures used for entire session and play game
#
if __name__ == '__main__':
    wordList = loadWords()
    playGame(wordList)


print playGame(wordList)
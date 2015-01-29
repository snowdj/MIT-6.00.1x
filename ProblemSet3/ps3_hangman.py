# 6.00 Problem Set 3
# 
# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random
import string

WORDLIST_FILENAME = "./words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = string.split(line)
    print "  ", len(wordlist), "words loaded."
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    result = True
    for char in secretWord:
        if char not in lettersGuessed:
            result = False
    return result

def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    result = ""
    for char in secretWord:
        if char in lettersGuessed:
            result += char
        else:
            result += "_ "
    return result

def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    import string
    allLetters = 'abcdefghijklmnopqrstuvwxyz'
    tempList = []
    result =""
    
    # Create lists with all letters
    for char in allLetters:
        tempList += [char]
    
    # Remove lettersGuessed from the list
    for char in lettersGuessed:
        tempList.remove(char)
    
    # Convert result to string
    for each in tempList:
        result += each
    
    return result     

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let tisWordGuessed(secretWord, lettersGuessed):he user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    
    print('Welcome to the game, Hangman!')
    print('I am thinking of a word that is '+str(len(secretWord))+' long.')
    print('-------------')
    
    # Initializion of variables
    guesses = 8
    lettersGuessed = []
    guessedWord = ""
    
    while guesses > 0:
        print('You have ' + str(guesses) + ' left.')
        AvailableLetters = getAvailableLetters(lettersGuessed)
        print('Available Letters: ' + AvailableLetters)
        guessedLetter = raw_input('Please guess a letter: ')
        guessedLetter = guessedLetter.lower()
        
        # Check if letter has already been guessed.  If so, send back to
        # beginning of loop    
        if guessedLetter in lettersGuessed:
            print("""Oops! You've already guessed that letter: """+ guessedWord)
            print('-------------')
            continue
            
        # Add newly guessed letter to the list of lettersGuessed
        lettersGuessed += [guessedLetter]
        
        # Check to see if the word has been guessed.  If so, congratulate and
        # complete the program.  If not, check for good or bad guess.
        # Good guess keeps the amount of guesses in tact.  Bad guess decrements
        # the number of guesses.
        guessedWord = getGuessedWord(secretWord, lettersGuessed)
        if not isWordGuessed(secretWord, lettersGuessed):            
            if guessedLetter in secretWord:
                print('Good guess: ' + guessedWord)
                print('-------------')
            else:
                print('Oops! That letter is not in my word: ' + guessedWord)
                print('-------------')
                guesses -= 1
                if guesses == 0:
                    print('Sorry, you ran out of guesses. The word was '+secretWord)
        else:
            print('Good guess: ' + guessedWord)
            print('-------------')
            print('Congratulations, you won!')
            break
   

# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

secretWord = chooseWord(wordlist).lower()
hangman(secretWord)

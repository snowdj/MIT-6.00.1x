def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE...
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
    # FILL IN YOUR CODE HERE...
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
    # FILL IN YOUR CODE HERE...
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
    
    return result.ascii_lowercase 
# 6.00 Problem Set 3
# 
# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import sys
import random
import string

WORDLIST_FILENAME = "words.txt"


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
    isGuessed = True
    for letter in secretWord:
        if letter not in lettersGuessed:
            isGuessed = False
    return isGuessed


def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...

    size = len(secretWord)
    guessedWordList = ['_'] * size    
        
    i = 0
    while( i < size):
        if secretWord[i] in lettersGuessed:
                guessedWordList[i] = secretWord[i]
        i += 1                
    guessedWord = ''.join(guessedWordList)
    return guessedWord
    
def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    alphabet = string.ascii_lowercase
    availableLetters = ''
    
    for letter in alphabet:
        if letter not in lettersGuessed:
            availableLetters += letter
    return availableLetters

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE...

    print 'Welcome to the game, Hangman!'
    print 'I am thinking of a word that is', len(secretWord), 'letters long.'
    
    guess = 8
    
    lettersGuessed = ['']
    
    while(guess > 0):
        print '_____________'
        print ''
        print 'You have', guess, 'guesses left.'
        print 'Available Letters:' + getAvailableLetters(lettersGuessed)
        user_input = raw_input('Please guess a letter: ').lower()
        if not (user_input in string.ascii_lowercase):
            print 'That is not a valid letter, Try again!'
            continue
        if (user_input in lettersGuessed):
            print 'Oops! You\'ve already guessed that letter:',getGuessedWord(secretWord, lettersGuessed)
        elif (user_input not in secretWord):
            lettersGuessed.append(user_input)
            print 'Oops! That letter is not in my word:', getGuessedWord(secretWord, lettersGuessed)
            guess -= 1
        elif (user_input in secretWord):
            lettersGuessed.append(user_input)
            print 'Good guess:', getGuessedWord(secretWord, lettersGuessed)
            if(isWordGuessed(secretWord, lettersGuessed)):
                break
        print ''
        
    print '_____________'
    print ''
    
    if(guess == 0):
        print 'Sorry, you ran out of guesses. The word was ' + secretWord + '.'

    else:
        print 'Congratulations, you won!'


secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
print '\nThanks for Playing!'

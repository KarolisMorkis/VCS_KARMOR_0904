HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

import random

words = ('ant baboon badger bat bear beaver camel cat clam cobra cougar '
         'coyote crow deer dog donkey duck eagle ferret fox frog goat '
         'goose hawk lion lizard llama mole monkey moose mouse mule newt '
         'otter owl panda parrot pigeon python rabbit ram rat raven '
         'rhino salmon seal shark sheep skunk sloth snake spider '
         'stork swan tiger toad trout turkey turtle weasel whale wolf '
         'wombat zebra ').split()

def RandomWord(words):
    wordIndex = random.randint(0, len(words) - 1)
    return words[wordIndex]

def DisplayBoard(missedLetters, correctLetters, secretWord):
    print(HANGMANPICS[len(missedLetters)])

    print ('Missed letters:')
    for letter in missedLetters:
        print(letter)
    print()

    blanks = "_"

    for i in range(len(secretWord)):
        if secretWord[i] in correctLetters:
            blanks = blanks[:i] + secretWord[i] + blanks[i+1:]
    for letter in blanks:
        print(letter)
    print()

def getGuess(alreadyGuessed):
    while True:
        print('Guess a letter:')
        guess = raw_input()
        guess = guess.lower()
        if len(guess) !=1:
            print('Ivesk tik viena raide')
        elif guess in alreadyGuessed:
            print('Raide jau panaudota, spek dar karta.')
        elif guess not in 'abcdefghijklmnopqrstuvwxyz':
            print('Iveskite raide')
        else:

            return guess

def playAgain():
    print ('Nori zaisti dar karta? (taip/ne)')
    return raw_input().lower().startswith('t')

print('H A N G M A N')
missedLetters = ''
correctLetters = ''
secretWord = RandomWord(words)
gameIsDone = False

while True:
    DisplayBoard(missedLetters, correctLetters, secretWord)
    guess = getGuess(missedLetters + correctLetters)
    if guess in secretWord:
        correctLetters = correctLetters + guess

        foundAllLetters = True
        for i in range(len(secretWord)):
            if secretWord[i] not in correctLetters:
                foundAllLetters = False
                break
            if foundAllLetters:
                print("Yes! The secret word is "' + secretWord + '"! You have Won!")
                gameIsDone = True
    else:
        missedLetters = missedLetters + guess

        if len(missedLetters) == len(HANGMANPICS) - 1:
            DisplayBoard(missedLetters, correctLetters, secretWord)
            print('You have run out of guesses!\nAfter ' + str(len(missedLetters)) + ' missed guesses and ' + str(len(correctLetters)) + ' correct guesses the word was "' + secretWord + '"')
            gameIsDone = True

    if gameIsDone:
        if playAgain():
            missedLetters = ''
            correctLetters = ''
            gameIsDone = False
            secretWord = RandomWord(words)
        else:
            break
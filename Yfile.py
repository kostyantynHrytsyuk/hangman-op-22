import random

def wordfill(guest):
    ''' 
    function fitch make from _*len
    to guested word
    '''
    global wordfilled



def game():
    print('Loading word list from file...')
    with ('words.txt') as fil:
        word=fil.readlines(random(0))
        amount=fil.lineamount
    print(amount,'words loaded.')
    print('Welcome to the game, Hangman!')
    print('I am thinking of a word that is',len(word),'letters long.')
    tryies=8
    letters=[]
    global wordfilled
    while tryies>0:
        print('------------')
        print('You have',tryies,'guesses left.')
        print('Available letters:',letters)
        guest=input('Please guess a letter: ')
        #try guest=
        if guest.lower in letters and guest in word:
            print('Good guess:',wordfill(guest))
            letters.pop(guest)
            if wordfilled==word:
                print('------------\nCongratulations, you won!')
                return True
        else:
            print('Oops! That letter is not in my word:',wordfilled)
            tryies-=1
    print('-----------\nSorry, you ran out of guesses. The word was else.')
    return False
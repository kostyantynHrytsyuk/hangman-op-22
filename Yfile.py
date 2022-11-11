def game(word):
    print('Loading word list from file...')
    #task of team_1
    # with ('words.txt') as fil:
    #     word=fil.readlines(random(0))
    #     amount=fil.lineamount
    #print(amount,'words loaded.')
    print('Welcome to the game, Hangman!')
    print('I am thinking of a word that is',len(word),'letters long.')
    tryies=8
    letters=[]# full alfavit of ungested 
    while tryies>0:
        print('------------')
        print('You have',tryies,'guesses left.')
        print('Available letters:',letters)
        guest=input('Please guess a letter: ')
        #task of team_3
        if guest.lower() in letters and guest in word:
            letters.pop(guest)
            for i in letters:
                wordfilled=word.replace(i,'_')
            print('Good guess:',wordfilled)
            if wordfilled==word:
                print('------------\nCongratulations, you won!')
                return True
        else:
            print('Oops! That letter is not in my word:',wordfilled)
            tryies-=1
    print('-----------\nSorry, you ran out of guesses. The word was else.')
    return False


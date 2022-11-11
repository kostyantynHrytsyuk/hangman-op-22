import random
def read_from_file(file_name):
    '''
    (list) -> (tuple)
    Creats new empty list. Reads the given file and writes each element into list. With random library chooses a word.
    Returns tuple first element of which - word,second lenght of list
    '''
    ranlist = []
    with open(file_name, "r") as file:
        for i in file:
            ranlist.append(i.split(' '))
    ranword = random.choice(ranlist[0])
    return ranword, len(ranlist[0])

def player_input(letters):
    '''
    Function checks if input is letter and returns it. Otherwise, function returns empty space.
    '''
    letters = letters.lower()
    if len(letters) != 1 or ord(letters) not in range(97, 123):
        return ''
    return letters

def output():
    '''
    Function makes an output according to the input.
    '''
    endgame = False
    guesses = 8
    letters = "abcdefghijklmnopqrstuvwxyz"
    word, list_len = read_from_file("words.txt")
    try_word = list(word)
    guessed_word = ["_ " for i in word]
    print(f"""Loading word list from file...
{list_len} words loaded.
Welcome to the game, Hangman!
I am thinking of a word that is {len(word)} letters long.""")
    while not endgame:
        print("-----------")
        print(f"""You have {guesses} guesses left.
Available letters: {letters}""")
        player_inp = input("Please guess a letter: ")
        if player_input(player_inp) == " ":
            print((f"Oops! Enter only 1 English letter"))
        elif player_input(player_inp) not in letters and player_input(player_inp) != " ": 
            print((f"Oops! You've already guessed that letter: {''.join(guessed_word)}"))
        elif player_input(player_inp) not in word:
            print((f"Oops! That letter is not in my word: {''.join(guessed_word)}"))
            letters = letters.replace(player_inp, "")
            guesses -= 1
        elif player_input(player_inp) in letters:
            letters = letters.replace(player_inp, "")
            for j in word:
                if  player_inp == j:
                    i = try_word.index(j)
                    try_word[i] = " "
                    guessed_word[i] = j
            print(f"Good guess:{''.join(guessed_word)}")
        if ''.join(guessed_word) == word:
            print("""------------\nCongratulations, you won!""")
            endgame = True
        elif guesses <= 0:
            print(f"""-----------\nSorry, you ran out of guesses. The word was '{word}'.""")
            endgame = True
output()
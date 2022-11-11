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

#вставте код двох інших команд
def output():
    endgame = False
    guesses = 8
    letters = "abcdefghijklmnopqrstuvwxyz"
    word = read_from_file("words.txt")[0]
    list_len = read_from_file("words.txt")[1]
    guessed_word = ["_ " for i in word]
    print(f"""Loading word list from file...
{list_len} words loaded.
Welcome to the game, Hangman!
I am thinking of a word that is {len(word)} letters long.""")
    while not endgame:
        print("-------")
        print(f"""You have {guesses} guesses left.
Available letters: {letters}""")
        player_inp = input("Please guess a letter: ")
        if player_input(player_inp) == " ":
            print((f"Oops! That letter is not in my word: {''.join(guessed_word)}"))
        if player_input(player_inp) not in letters:
            print((f"Oops! You've already guessed that letter: {''.join(guessed_word)}"))
        else:
            letters = letters.replace(player_inp, "")
        for i,j in word:
            if  player_inp==j:
                guessed_word[i] = j
        print(f"Good guess:{''.join(guessed_word)}")
        if win:
            print("win_msg")
            endgame = True
        if lose:
            print("lose_msg")
            endgame = True
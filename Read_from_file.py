import random

def read_from_file(file_name):
    '''
    (list) -> (str)
    Creats new empty list. Reads the given file and writes each element into list. With random library chooses a word.
    '''
    ranlist = []
    with open(file_name, "r") as file:
        for i in file:
            ranlist.append(i.split(' '))
    ranword = random.choice(ranlist[0])
    return ranword, len(ranlist[0])

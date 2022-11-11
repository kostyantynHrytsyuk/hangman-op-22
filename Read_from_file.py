import random

def read_from_file(file_name):
    '''
    (str) -> (tuple)
    Creats new empty list. Reads the given file and writes each element into list. With random library chooses a word.
    Returns tuple first element of which - word,second lenght of list
    '''
    ranlist = []
    if isinstance(file_name , str):
        with open(file_name, "r") as file:
            for i in file:
                if isinstance(i , str):
                    ranlist.append(i.split(' '))
                    ranword = random.choice(ranlist[0])
                    return ranword, len(ranlist[0])
    else:
        return None , None

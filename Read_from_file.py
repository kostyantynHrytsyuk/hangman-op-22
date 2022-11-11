import random

def read_from_file(file_name):
    ranlist = []
    with open(file_name, "r") as file:
        for i in file:
            ranlist.append(i.split(' '))
    ranword = random.choice(ranlist[0])
    return ranword, len(ranlist[0])

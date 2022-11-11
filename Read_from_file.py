import random

def read_from_file(file_name):
    ranlist = []
    with open(file_name, "r") as file:
        for i in file:
            ranlist.append(i.split(' '))
    return ranlist[0]
print(read_from_file("words.txt"))
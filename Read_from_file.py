import random

def read_from_file(file_name):
    ranlist = []
    with open(file_name, "r", endcoding='utf-8') as file:
        for i in file:
            ranlist.append(i)
    return ranlist
print(read_from_file("words.txt"))
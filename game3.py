def player_input():
    '''
    Function checks if input is letter and returns it. Otherwise, function returns empty space.
    '''
    letters = input()
    letters = letters.lower()
    if len(letters) == 1 and ord(letters) in range(97, 123):
        return letters
    else:
        return ' '
print(player_input())

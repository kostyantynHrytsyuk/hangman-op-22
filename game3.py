def player_input():
    '''
    Function checks if input is letter and returns it. Otherwise, function returns empty space.
    '''
    letters = input()
    letters = letters.lower()
    if len(letters) != 1 or ord(letters) not in range(97, 123):
        return ''
    return letters
    
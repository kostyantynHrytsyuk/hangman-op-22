def player_input(letters):
    '''
    '''
    if isinstance(letters, str):
        letters = letters.lower()
        if len(letters) == 1 and ord(letters) in range(97, 123):
            return letters
        else:
            return False
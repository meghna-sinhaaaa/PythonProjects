#!/usr/bin/env python3

def character_frequency(filename):
    """Counts the frequency of each character in the given file."""
    # first try to open the file
    try:
        f = open(filename)
    except OSError:
        return None
        
    #Now process the file
    characters = {}
    for line in f:
        for char in line:
            characters[char] = characters.get(char,0) + 1
    f.close()
    return characters
    
#raising errors

def validate_user(username, minlen):
    assert type(username) == str, "username must be a string"
    if minlen < 1:
        raise ValueError("minlen must be atleast 1")
    if len(username) < minlen:
        return False
    if not username.isalnum():
        return False
    return True
    
#testing for expected errors

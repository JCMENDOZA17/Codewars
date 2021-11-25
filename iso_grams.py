def is_isogram(string):
    assert isinstance(string, str)
    new_string = string.lower()

    for letter in new_string:
        if new_string.count(letter) == 1:
            continue
        else:
            return False
    return True    
    



if __name__ == '__main__':
    assert is_isogram("Dermatoglyphics") == True
    assert is_isogram("isogram") == True
    assert is_isogram("aba") == False
    assert is_isogram("moOse") == False
    assert is_isogram("isIsogram") == False
    assert is_isogram("") == True
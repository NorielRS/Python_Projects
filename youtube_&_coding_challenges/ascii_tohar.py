# chr(69) shows character
# ord('c') shows numbers

def counterpartCharCode(char):

    if (char.isupper()):
        return ord(char.lower())
    else:
        return ord(char.upper())
        


print(counterpartCharCode('a'))


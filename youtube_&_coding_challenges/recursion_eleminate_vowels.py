def eleminate_vowels(word):
    vowels = 'aeiou'

    if len(word) == 0:
        return word
    # elif word[0] not in vowels:
    #     return word[0] + eleminate_vowels(word[1:])
    else:
        return word[0] + str(eleminate_vowels(word[1:])) if word[0] not in vowels else eleminate_vowels(word[1:])
   




print(eleminate_vowels('celebrate'))
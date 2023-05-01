words = 'celebration'
vowels = 'aeiou'
newStr = ''

for i in range(len(words)):
    # if vowels.find(words[i]) == -1:
    #     newStr += words[i]
    if words[i] not in vowels:
        newStr += words[i]

print(newStr)
#    LEARN SUBSTRINGS IN PYTON!!
        

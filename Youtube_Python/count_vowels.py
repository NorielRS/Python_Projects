words = 'CLEBRATION'

vowels = 'aeiou'

count = 0

for i in words.lower():
    if i not in vowels:
        count+=1

print(len(words)-count)
givenStr = 'xoxoxoxo'
Count = 0


# check the number of o\x

for i in givenStr.lower():
    if i == 'x':
        Count+=1
    elif i == 'o':
        Count-=1
    else: 
        result = True

result = (Count == 0)

print(result)

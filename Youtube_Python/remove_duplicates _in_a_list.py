numbers = [2,2,3,4,5,5,1,5]
newNum =[]

for number in numbers:
    if number not in newNum:
        newNum.append(number)

print(newNum)
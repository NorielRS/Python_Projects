import random
myList = []

while True:

    question = input('Enter a question: ')
    answer = input('Enter Answer: ')

    myTuple = (question, answer)
    myList.append(myTuple)

    randNum = random.randint(0, len(myList) - 1)
    print(myList[randNum])
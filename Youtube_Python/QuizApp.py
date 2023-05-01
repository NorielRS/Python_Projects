import random

myList = []
breaker = 0




while breaker < 3:

    question = input('Enter a question: ')
    answer = input('Enter Answer: ')

    myTuple = (question, answer)

    myList.append(myTuple)
    breaker+=1




print('--------START QUIZ----------')


while True:

    randomQuestionList =[]
    randNum = random.randint(0, len(myList) - 1)

    randomQuestionList.append(myList[randNum])


    for Q, CA in randomQuestionList:

        ans = input(f"""{Q}
""")

        if ans == CA:
            print("Correct!")
        else:
            print(f"The answer is {CA!r}, not {ans!r}")






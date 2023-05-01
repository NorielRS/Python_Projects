operator = input('Enter Math Operator: ')
try:
    firstNumber = int(input('Enter First Number: '))
    secondNumber = int(input('Enter Second Number: '))

except ValueError:
    print('Wrong Input, Try Again')
    firstNumber = int(input('Enter First Number: '))
    secondNumber = int(input('Enter Second Number: '))
    

if operator =='+':
    result =  firstNumber + secondNumber
elif operator == '-':
    result =  firstNumber + secondNumber
elif operator == '*':
   result =  firstNumber + secondNumber
elif operator == '/':
   result =  firstNumber + secondNumber

print(result)


list =[]

result = int(input('first num:'))
list.append(result)

while True:
    oper = input("operator:")
    num = int(input("number:"))
    list.append(num)

    

    
    if oper =='+':
         result = result + list[1]
    elif oper == '-':
        result = result - list[1]
    elif oper == '*':
        result = result*list[1]
    elif oper == '/':
        result = result/list[1]
    else:
        break

    list.pop(1)


    print(result)
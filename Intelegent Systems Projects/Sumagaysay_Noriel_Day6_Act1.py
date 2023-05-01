# RECORD KEEPING APP

record = {'Lastname':''}

while True:
    action = input('''
    
    a. Add Data
    b. Delete Data
    c. End
   
    >> ''')

    if action == 'a':
        input_key = input('Enter Key: ')
        input_value = input('Enter Value: ')

        record[input_key] = input_value
        print(' ')
        print(record)

    elif action == 'b':
        input_key = input('Enter Key: ')
        del record[input_key]
        print(' ')
        print(record)

    elif action == 'c':
        print('THANK YOU')

        break

    else:
        print('Wrong input, Try again!')


    

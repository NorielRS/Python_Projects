def fizz_buzz(input_number):
    if input_number % 3 == 0 and input_number % 5 == 0:
        return '"FizzBuzz"'
    elif input_number % 3 == 0:
        return '"Fizz"'
    elif input_number % 5 == 0:
        return '"Buzz"'
    else:
        return '"'+str(input_number) + '"'



print(fizz_buzz(4))
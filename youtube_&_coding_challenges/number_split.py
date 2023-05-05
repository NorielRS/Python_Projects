def number_split(number):
   
    n = int(number / 2)

    return  [n,n+1] if number  % 2 == 1 else [n,n]

    # if number % 2 == 1:
    #     return [n,n+1]
    # else:
    #     return[n,n]

    


print(number_split(8))
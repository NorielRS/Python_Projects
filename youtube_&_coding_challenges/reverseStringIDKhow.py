# print('hello'[::-1])

def str_reverse(mystr):
    
    
    if len(mystr) == 0:
        return mystr
    else:
        return mystr[-1] + str_reverse(mystr[:-1])


print(str_reverse("hello"))

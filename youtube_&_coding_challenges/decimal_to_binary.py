def binary(mydecimal):

    binary_result = ''

    while mydecimal > 0:
        
        if mydecimal % 2 ==1:
            binary_result = '1'+binary_result
            mydecimal = int(mydecimal /2)
        else:
            binary_result = '0'+binary_result
            mydecimal = int(mydecimal /2)


    return binary_result




print(binary(17))
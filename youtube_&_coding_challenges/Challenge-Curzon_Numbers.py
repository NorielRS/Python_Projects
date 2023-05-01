def is_curzon(num):
    squaredValue = 2 ** num + 1
    mulValue = 2 * num + 1

    

    if squaredValue % mulValue == 0:
        return True

    elif squaredValue % mulValue != 0:
        return False

    

# print(is_curzon(10))

print(is_curzon(14))


print(33 % 11)
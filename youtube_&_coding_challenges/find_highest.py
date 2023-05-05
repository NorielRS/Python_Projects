def find_highest(given_list):
    if len(given_list) == 1:
        return given_list[0]
    else:
        m = find_highest(given_list[1:])
        return m if m > given_list[0] else given_list[0]

def recursive_max(a):
    if len(a) ==1:
        return a[0]
    else:
        return a[0] if a[0] > recursive_max(a[1:]) else recursive_max(a[1:])


print('recursive max is ',recursive_max([0, 12, 4, 87]))
print('find highest is',find_highest([0, 12, 4, 87]))



# # Recursion example
# def tri_recursion(k):
#   if(k>0):
#     result = k+tri_recursion(k-1)
#     print(result)
#   else:
#     result = 0
#   return result

# print("\n\nRecursion Example Results")
# tri_recursion(5)


# # Program to print factorial of a number
# # recursively.

# # Recursive function
# def recursive_factorial(n):
#     if n == 1:
#         return n
#     else:
#         return n * recursive_factorial(n-1)

# # user input
# num = 6

# # check if the input is valid or not
# if num < 0:
#     print("Invalid input ! Please enter a positive number.")
# elif num == 0:
#     print("Factorial of number 0 is 1")
# else:
#     print("Factorial of number", num, "=", recursive_factorial(num))

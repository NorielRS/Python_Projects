# matrix =[
#     ['A','B','C'],
#     ['D','E','F'],
#     ['G','H','I']
# ]
matrix = [
    [1,1,0],
    [0,1,1],
    [1,0,1]
]
for row in range(matrix.__len__()):
    for col in range(matrix.__len__()):
        if matrix[row][col] == 0:
            matrix[row][col] = 1
        

print(matrix)
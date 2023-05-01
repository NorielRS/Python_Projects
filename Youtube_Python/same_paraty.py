def paraty_analysis(number):

    toSeperate = str(number)
    totalFinal = 0
    for i in range(len(toSeperate)):
        totalFinal += int(toSeperate[i])

    if number % 2 == 0 and totalFinal % 2 == 0 or number % 2 == 1 and totalFinal % 2 == 1:
        return 'True'  
    else:
        return 'False'








print(paraty_analysis(3))


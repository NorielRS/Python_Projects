def find_highest(given_list):
    i = 1
    highest = given_list[0]
    if highest > given_list[i]:
        return highest
    else:
        i+1
        return find_highest(given_list)








print(find_highest([0, 12, 4, 87]))

def jazzify(GivenList):
    newlist = []
    for i in GivenList:
        if '7' in i:
            newlist.append(i)
        else:
            newlist.append(i + '7')
    return newlist

print(jazzify(['a', 'b', 'c','77']))


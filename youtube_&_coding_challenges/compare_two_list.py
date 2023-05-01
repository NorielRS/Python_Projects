# COMPARING LIST WITH SIMILAR ELEMENTS

firstList =[1,10,20,30]
secondList =[1,30,10,20]
same = True

for i in firstList:
    if i not in secondList:
        same = False

print(same)


# COMPARING LIST WITH THE SAME ELEMENT IN THE SAME INDEX

def compare_list(list1,list2):

    if list1 == list2:
        return True
    elif list1 != list2:
        return False
    else:
        return ' Not Working'


print(compare_list([3,2,1], [3,2,1]))

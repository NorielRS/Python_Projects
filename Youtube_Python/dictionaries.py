# dictionaries sa python, HashMap sa java

number = input("Number: ")

NumWords = {
    "1": "one",
    "2": "two",
    "3": "three",
    "4": "four"
}

emptyString = ""
for i in number:
    emptyString+=NumWords.get(i,i+" ") + " "#yung pangalawang i sa loob,
    #  yung value noon ang replacement pag walang kapareho sa loob ng dictionary

print(emptyString +"!")
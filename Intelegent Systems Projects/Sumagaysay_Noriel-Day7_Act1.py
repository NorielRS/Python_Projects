import random

firstnames = ['ha','he','hu']
middlenames = ['du', 'la', 't']
lastnames = ['ken','man','dog']

firstname = random.randint(0, len(firstnames)-1)
middlename = random.randint(0, len(middlenames)-1)
lastname = random.randint(0, len(lastnames)-1)

print(f'{firstnames[firstname]}{middlenames[middlename]}{lastnames[lastname]}' ) 
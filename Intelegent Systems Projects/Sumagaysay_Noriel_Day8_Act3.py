class Student:
    def __init__(self, name, math, science, english):

        avarage = (math + science + english)/3

        if avarage >= 75: stat = 'passed'
        
        else: stat = 'failed'

        print(f'''
name: {name}
Math: {math}
Science: {science}
English: {english}
Avarage: {avarage} {stat}
        ''')


name = 'Alex'
math = 90
science = 85
english = 80
st = Student(name, math, science, english)
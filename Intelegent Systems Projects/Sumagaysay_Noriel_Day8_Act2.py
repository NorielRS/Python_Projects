class Employee:
    def __init__(self, name, email, mobileNumber):
        self.name = name
        self.email = email
        self.mobileNumber = mobileNumber

        print(f'''Name: {name}
Email: {email}  
Number: {mobileNumber}   
        ''')


emp1 = Employee("ha", "du", "ken")
emp2 = Employee("ha", "la", "man")
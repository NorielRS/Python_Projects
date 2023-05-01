# SALARY COMPUTATION APP
# MAIN
from GrossSalary import grossSalary
from SalaryDeduction import salaryDeduction
from NetSalary import netSalary


name = input('Enter name: ')
hours = float(input('Enter Hours of Work: '))
loan = float(input('Enter Loan Value: '))
health_insurance = float(input('Enter Health Insurance Value: '))

gross = grossSalary(hours)
deduction = salaryDeduction(gross, loan, health_insurance)
net = netSalary(deduction,gross)

print(net)
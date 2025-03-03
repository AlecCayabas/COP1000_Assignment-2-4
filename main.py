# input statements
salary = float(input())
numDependents = float(input())

# calculate taxes here
stateTax = 0.065
federalTax = .28
depedentDeduction = 0.025 * salary * numDependents
totalWitholding: stateTax + federalTax + dependentDeduction
takeHomePay = salary - totalWitholding

# output statements
print("Salary: $" + str(salary))
print("Take Home Pay: $" + str(takeHomePay))

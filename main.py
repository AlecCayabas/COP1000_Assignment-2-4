# input statements
salary = float(input("Enter your salary: "))
numDependents = float(input("Enter your number of dependents: "))

# calculate taxes here
stateTax = salary * 0.065
federalTax = salary * 0.28
dependentDeduction = (0.025 * salary) * numDependents
totalWitholding = (stateTax + federalTax) + dependentDeduction
takeHomePay = salary - totalWitholding

# output statements
print("State Tax: $" + str(stateTax))
print("Federal tax: $" + str(federalTax))
print("Dependents: $" + str(dependentDeduction))
print("Salary: $" + str(salary))
print("Take Home Pay: $" + str(takeHomePay))


name = input("Enter name: ")
salary = float(input("Enter basic salary: "))

if salary >= 50000:
    bonus = salary * 0.10
    tax = salary * 0.05
elif salary >= 30000:
    bonus = salary * 0.07
    tax = salary * 0.03
else:
    bonus = salary * 0.05
    tax = salary * 0.01

fsalary = salary + bonus - tax

print("Name:", name)
print("Basic Salary:", salary)
print("Bonus:", bonus)
print("Tax:", tax)
print("Final Salary:", fsalary)

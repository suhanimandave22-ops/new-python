n = int(input("Enter number of students: "))

for i in range(n):
    print("\nStudent", i+1)
    name = input("Enter name: ")
    total = 0

    sub1 = int(input("Enter marks of computer: "))
    sub2 = int(input("Enter marks of English: "))
    sub3 = int(input("Enter marks of c: "))
    sub4 = int(input("Enter marks of python: "))
    sub5 = int(input("Enter marks of electtronic: "))
    total = sub1+sub2+sub3+sub4+sub5 

    percentage = total / 5

    print("Name:", name)
    print("Total:", total)
    print("Percentage:", percentage)

    if percentage >= 75:
        print("Grade: A")
        print("Result: PASS")
    elif percentage >= 60:
        print("Grade: B")
        print("Result: PASS")
    elif percentage >= 40:
        print("Grade: C")
        print("Result: PASS")
    else:
        print("Grade: F")
        print("Result: FAIL")

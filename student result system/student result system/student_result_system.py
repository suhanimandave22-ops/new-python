for i in range(1, 6):
    print("\nStudent", i)

    name = input("Enter name: ")

    marks1 = int(input("Enter marks of Computer: "))
    marks2 = int(input("Enter marks of Maths: "))
    marks3 = int(input("Enter marks of elect: "))
    total = marks1+marks2+marks3

    percentage = total / 3

    print("Name:", name)
    print("Total Marks:", total)
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
        print("Grade: Fail")

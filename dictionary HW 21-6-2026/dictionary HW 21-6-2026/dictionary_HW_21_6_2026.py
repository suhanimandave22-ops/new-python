students={}
while True:
    print("------------------------------------------------")
    print("\n1.Add student \n2.display student result \n3.subject topper and lowest \n4.exit")
    print("------------------------------------------------")
    choice=int(input("enter your choice:"))
    match choice:
      case 1: 
        name=input("Enter student name:")
        marks={
                "Math":int(input("Math Marks: ")),
                "Science":int(input("Science Marks: ")),
                "English":int(input("English Marks: "))
        }
        students[name]=marks
        print("student details added successfully!")
      case 2:
        if not students:
            print("student result not found")
        else:
            print("\nStudent results")
            print("-----------------------------------------")
            for name,marks in students.items():
                total=sum(marks.values())
                perc=total/len(marks)

                print("Name:",name)
                print("Total:",total)
                print("percentage:",perc)
                print("-----------------------------------------")
         
      case 3:
        print("all Subject topper and lowest")
        if not students:
                print("No students found")
        else:
                subjects = ["Math", "Science", "English"]

                for subject in subjects:
                    topper = None
                    lowest = None
                    max_marks = -1
                    min_marks = 101

                    for name, marks in students.items():
                        score = marks[subject]

                        if score > max_marks:
                            max_marks = score
                            topper = name

                        if score < min_marks:
                            min_marks = score
                            lowest = name

                    print(f"\nSubject: {subject}")
                    print(f"Topper: {topper} ({max_marks})")
                    print(f"Lowest: {lowest} ({min_marks})")

      case 4:
        print("exit")

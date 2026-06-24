#x=[[10,20],[11.2,12.3],"hi",90]
#print 12.3
#print(x)
#print(x[1])
#print(x[1][1])
#print(x[2])
#print(x[3])
#for i in x:
 #   print(i)

#for i in x:
 #   if type(i)==list:
 
#for j in i:
#            print(j)
 #   continue
#print(i)

#student=[[101,"Ram",98],
 #        [102,"Sita",88],
  #       [103,"Ramu",78],
   #      [104,"gita",99]]
#for i in student:
 #   print(i[0])
#for i in student:
#    print(f"{i[1]}-->{i[2]}")

    #add using append
#student.append([105,"komal",55])
#print(student)

#user ip
#id=int(input("Enter id:"))
#name=input("Enter name:")
#marks=int(input("Enter marks:"))
#student.append([id,name,marks])
#print(student)

students=[]

while True:
    print("SMS\n1.add\n2.View\n3.update\n4.delete\n5.Topper\n6.exit\n")
    choice=int(input("Enter your choice:"))
    match choice:
        case 1:
            ip=int(input("how many student data do u want to add\n"))
            for i in range(ip):
                id=int(input("enter your id:\n"))
                name=input("Enter your name:")
                marks=int(input("Enter your marks:"))
                students.append([id, name, marks])
            print("Student record added successfully")                

        case 2:
            if not students:
                print("Student record not found")
            else:
                print("\nStudent record:")
                for s in students:
                    print(f"\nId:{s[0]} \nName:{s[1]}\nMarks:{s[2]}")
        case 3:
            id = int(input("Enter student id to update:"))
            for s in students:
                if s[0]==id:
                    s[1]==

        case 4:
            pass
        case 5:
            pass
        case 6:
            print("Thanks for using SMS!")
            exit()
        case _:
            print("invalid input !")
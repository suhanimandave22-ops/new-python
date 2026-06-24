
print("------------String Programmming------------")
print("\n 1.Reverse String\n 2.Check palindrome\n 3.Convert slicing (Uppercase, Lowercase,Swapcase)\n 4.Count Words\n")
print("-------------------------------------------")
num=int(input("Enter your choice:"))

match num:
    
    case 1:
        x=input("Enter a string:")
        rev=x[::-1]
        print("Reversed String:",rev)
    case 2:
        x=input("Enter a string:")
        if x==x[::-1]:
            print("Its a palindrome")
        else:
            print("Not a palindrome")
    case 3:
        x=input("Enter a string:")
        print("-----------------------------------")
        print("\n1.Uppercase\n2.Lowercase\n3.Swapcase")
        print("-----------------------------------")
        choice=int(input("Enter your choice:"))
        
        if(choice==1):
                print("Uppercase:",x.upper())
        elif(choice==2):
                print("Lowercase:",x.lower())
        elif(choice==3):
                print("Swapcase:",x.swapcase())
    case 4:
        x=input("Enter a string:")
        words=x.split()
        print("Total words:",len(words))

    case _:
        print("Invalid input")
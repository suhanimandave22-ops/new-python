for i in range(3):
    for j in range(3):
        if i==j or i+j==2:
            print("*",end=" ")
        else:
            print("0",end=" ")
    print()

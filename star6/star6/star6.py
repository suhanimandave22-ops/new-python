for i in range(4):
    for j in range(4):
        if i==0 or i==3:
            if j==0 or j==3:
                print("0", end=" ")
            else:
                print("*",end=" ")
        else:
            if j==0 or j==3:
                print("*",end=" ")
            else:
                print(" ", end=" ")
    print()

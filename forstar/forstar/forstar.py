n=3
for i in range(1,n+1):
    for j in range(3):
        print(i,end=" ")
    print()

print()

n=0
for i in range(3):
    for j in range(3):
        n+=1
        print(n,end=" ")
    print()
print()

n=3
for i in range(n):
    for j in range(n):
        if i==j:
            print("1",end=" ")
        else:
            print("0",end=" ")
    print()
print()

n=1
for i in range(1,n+1):
    for j in range(1,n+1):
        if i==1 or i==4 or j==1 or j==4:
            print("X",end=" ")
    print()

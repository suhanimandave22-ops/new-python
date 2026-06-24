n=int(input("Enter a number:"))
b=""
while n!=0:
    rem=n%2
    b=str(rem)+b
    n//=2
print("Binary no:",b)
num = 145
temp = num
s = 0
while temp > 0:
    digit = temp%10
    fact = 1
    for i in range(1, digit+1):
        fact *= i
    s+=fact
    temp//=10
if s == num:
    print("Strong number")
else:
    print("Not strong number")
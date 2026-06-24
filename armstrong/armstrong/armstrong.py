num=int(input("Enter a number:"))
temp=num
count=0
sum=0
while temp>0:
    count+=1
    temp//=10
print(count)
temp=num
while temp>0:
    rem=temp%10
    sum+=(rem**count)
    temp//=10
if sum==sum:
    print("armstrong")
else:
    print("Not armstrong")

num=28
while num!=1 and num!=4:
    sum=0
    while num>0:
        rem=num%10
        sum+=rem*rem
        num//=10
    num=sum
if num==1:
    print("happy")
else:
    print("not happy")

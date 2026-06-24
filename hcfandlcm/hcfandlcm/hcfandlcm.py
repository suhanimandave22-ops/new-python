a=int(input("Enter first number:"))
b=int(input("Enter second number:"))

hcf=1
for i in range(1,min(a,b)+1):
    if a%i==0 and b%i==0:
        hcf=i
lcm=max(a,b)
while lcm%a!=0 or lcm%b!=0:
    lcm+=1
print("HCF:",hcf)
print("LCM:",lcm)


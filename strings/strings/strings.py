name="ram"
print(name)
print(id(name))
print(name[0])
name="sita"
print(name)
print(id(name))

for ch in name:
    print(ch)

  #reverse
x="maharashtra"
print(len(x))
for ch in range(len(x)-1,-1,-1):
    print(x[ch])

#count

x="india"
ct=0
for ch in x:
    ct+=1
print(ct)

#methods
x="India"
print(x.upper())
print(x.lower())
x="hello how are you?"
print(x.title())
print(x.capitalize())

x="India"
print(x.swapcase())
print(x.replace('dia','x')) #replaces the substring(dia) with the new string(x)

x="india"
print(x.replace('i','z')) #replaces all the occurrences of the substring(i) with the new string(z)

#split method
x="apple ,banana ,grapes"
print(x.count('p'))
print(x.index('e'))
print(x.find('v')) #returns -1 if the substring is not found
print(x.split(','))

#checking the methods are true or false
x="hello"
print(x.isupper())
print(x.islower())

print(x.isalpha()) #checks the alpha characters only
print(x.isdigit()) #checks the digit characters only

x="a1234"
print(x.isalnum()) #checks the alpha and digit character only

print(x.startswith("a1"))
print(x.startswith("cal"))
print(x.endswith("4"))

#white spaces remove
x="   hello"
print(x.rstrip())#removes the white spaces from the right side
print(len(x)) 
x=x.strip() #removes the white spaces from both sides
print(len(x)) 
print(x.lstrip())#removes the white spaces from the left side

a=input("enter name:")
ip=input("enter char to check:")
ct=0
for ch in a:
    if(ch==ip):
     ct+=1
print(ct)

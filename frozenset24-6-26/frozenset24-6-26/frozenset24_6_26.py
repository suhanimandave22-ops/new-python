x=frozenset([1,2])
print(x,type(x))

roles=frozenset(["admin","faculty","receptionist"])
for i in roles:
    if i=="admin":
        print(i)

#roles.add("hacker") #throws an error

def greet():
    print("Hello")
greet()
'''#no return type no argument
def greet():
    print("Welcome user!")
greet()#function call-->function args
greet()
print("--------------------------------------------1")

#no return type with argument
def greet1(name):
    print("welcome ", name)

greet1("suhani")
print("--------------------------------------------2")

#user input function
def greett(name):
    print("Welcome",name)
name=input("Enter your name:")
greett(name)
print("--------------------------------------------3")

def getno():
    return 10**2

print(getno())
print("--------------------------------------------4")
#value use
op=getno()
print(op)
op+=2
print(op)
print("--------------------------------------------5")
#with return type with args

def cube(num):
    return num**3
num=int(input("Enter a number:"))
print(cube(num))
print("--------------------------------------------6")

#
def add(a,b):
    print(a+b)
add(10,20)
print("--------------------------------------------7")

#*args
def add1(*args):
    print(sum(args))
    print(type(args))
add1(1,2,3,5765,90)
print("--------------------------------------------8")

def info(name,age,marks):
    return f"name:{name}\n age:{age}\n marks:{marks}"
name=input("Enter your name:")
age=int(input("Enter your age:"))
marks=float(input("Enter your marks:"))
print(info(name,age,marks))
'''
#basic calculator:

def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def mul(a,b):
    return a*b

def div(a,b):
    if a==0 or b==0:
        print("Cannot divide by 0")
    else:
        return a/b

a=int(input("Enter first number:"))
b=int(input("Enter second number:"))

print("1.Additon\n2.Substraction\n3.Multiplication\n4.Division")
ch=int(input("choose a number:"))
match ch:
    case 1:
        print(add(a,b))
    case 2:
        print(sub(a,b))
    case 3:
        print(mul(a,b))
    case 4:
        print(div(a,b))
    case _:
        print("invalid")
###########################################
'''
def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def mul(a,b):
    return a*b

def div(a,b):
    if a==0 or b==0:
        print("Cannot divide by 0")
    else:
        return a/b

a=int(input("Enter first number:"))

print("1.+\n2.-\n3.*\n4./")
ch=int(input("choose a operator:"))
if ch==1:
    print(a,"+")
elif ch==2:
    print(a,"-")
elif ch==3:
    print(a,"*")
elif ch==4:
    print(a,"/")
else:
    print("invalid")

b=int(input("Enter second number:"))
if ch==1:
    print(a,a+b)
elif ch==2:
    print(a-b)
elif ch==3:
    print(a*b)
elif ch==4:
    print(a/b)
    
nums = list(map(float, input("Enter numbers separated by space: ").split()))

print("\nChoose operator: +  -  *  /")
op = input("Enter operator: ")

match op:
    case "+":
        print("Result:", add(*nums))

    case "-":
        print("Result:", sub(*nums))

    case "*":
        print("Result:", mul(*nums))

    case "/":
        print("Result:", div(*nums))

    case _:
        print("Invalid operator")'''
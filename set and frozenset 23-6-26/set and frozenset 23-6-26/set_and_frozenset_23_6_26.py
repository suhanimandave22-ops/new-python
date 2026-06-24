#set
x={10,20}
print(x,type(x))
print("-------------------------1")

#user ip
x=set()
x.add(10)
print(x,type(x))
print("-------------------------2")

#loop 
x={10,20,30,40,10,20}
print(x)
for item in x:
    print(item)
print("--------------------------3")

#functions and method
  #add
x.add(90)
print(x)
print("--------------------------4")

  #remove
x.remove(10)
print(x)
print("--------------------------5")

 #discard  : it also work as a remove method
x.discard(20)
print(x)
x.discard(7)
print(x)
print("--------------------------6")
 
 #clear
x.clear()
print(x)
print("--------------------------7")

  #copy
a={1,2}
b=a.copy()
print(b)
print("--------------------------8")

  #update
a.update([10,20,30])
print(a)
print("--------------------------9")

# table 1 and table 2
a={1,2,3}
b={3,4,5}
print(a)
print(b)
print("--------------------------10")

# table 1 and table 2------>entire----> duplicate ignore
print(a.union(b))
print(a|b)
print("--------------------------11")

#common data ---->intersection &
print(a.intersection(b))
print(a&b)
print("--------------------------12")

#data from table 1
print(a.difference(b))
print(a-b)
print("--------------------------13")

#symmetric difference
print(a.symmetric_difference(b))
print(a ^ b)
print("--------------------------14")

py_stud={"ram","sita","komal","ramu"}
jv_stud={"ram","pavan","gita"}
fd_stud={"gita","komal","payal","ram"}

#total count of each
all=py_stud|jv_stud|fd_stud
print(len(all))
print("--------------------------15")

#name of stud who are attending py , jv 
print(py_stud|jv_stud)
print("--------------------------16")

#who are attending java ,python and fd
print(py_stud|jv_stud|fd_stud)
print("--------------------------17")

#only jv
print(jv_stud)
print("--------------------------18")

#only py
print(py_stud)
print("--------------------------19")

#name of stud who are not attending py , jv 
print(fd_stud-(jv_stud|py_stud))
print("--------------------------20")

#name of stud who attend 3 batches at time

#name of stud who attend 1 batch at a time

for stud in all:
    count=0
    if stud in py_stud:
        count+=1
    if stud in jv_stud:
        count+=1
    if stud in fd_stud:
        count+=1
    if count==1:
        print(stud)
print("--------------------------21")

set1={12,35,8,25,5}
set2={25,6,35,15,8}
 
alln=set1|set2
#divisible by 5
for i in alln:
    if i%5==0:
        print(i)
print("--------------------------22")

#even sum=?
sum=0
for i in alln:
    if i%2==0:
        sum+=i
        print(i)
print("sum:",sum)
print("--------------------------23")

#common element sum-->sq-->cube
com=set1&set2
print(com)
sum=0
sq=0
cube=0
for i in com:
    sum+=i
print("sum:",sum)
sq=sum*sum
print("sq:",sq)
cube=sq*sq*sq
print("cube:",cube)
print("--------------------------24")

#mul of non repeating no
non_rep=set1^set2
mul=1
for i in non_rep:
    mul*=i
print(mul)
print("--------------------------25")

'''features
1.unique
2.unordered structure
3.mutable'''



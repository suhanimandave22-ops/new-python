x=[10,20,30]
#access 20
print(x)
print(x[1])
#update: refvar[index]=newvalue
print(x[2])
x[2]=300
print(x[2])

#list using loop
x=[10,20,30]
for item in x:
    print(item)

#append: add new item to the end of the list
#add element by taking user input
x=[]
print(x)
for i in range(5):
    ip=input(f"Enter {i+1} element:")
    x.append(ip)
print(x)

#extend : add multiple items to the end of the list
x=[1,2,3]
print(x)
x.extend([4,5,6])
print(x)

#insert(index:value):add new item at the declared index or specified position
x=[11,12]
x.insert(1,12)
print(x)

#remove(element)/pop (index)
x=[10,8,9,"hi",90,89]
x.remove("hi")
x.pop(4)
print(x)

#clear:remove all items from the list
x.clear()
print(x)

x=[10,20,40,60,10,30]
#count: count the number of times an element appears in the list
print(x.count(10))
#index:return the index number
print(x.index(30))
#sort the list in asceding order
x.sort()
print(x)
#reverse the list
x.reverse()
print(x)
#copy create a copy of the original list
y=x.copy()
print(y)

#function
x=[78,90,12,8]
print(len(x))
print(max(x))
print(min(x))
print(sum(x))
print(sorted(x,reverse=True))

#count without using function
x=[10,20,30]
count=0
for i in x:
    count+=1
print(count)

#max without using function 
x=[10,20,30,45,5]
max=0
for i in x:
    if i>max:
        max=i
print(max)

min=x[0]
for i in x:
    if i<min: #10<10f 20<10f 30<10f 45<10f, 5<10 True
        min=i
print(min)

#student=[1,"ram",2,"sita",3,"pooja"]
#print(student)
#for i in range(len(student)):
#   if i%2==0:
#        print(student[i])

#student=[1,"ram",2,"sita",3,"pooja"]
#for i in range(len(student)):
#    if i%2!=0:
 #       print(student[i])

student=[1,"ram",45,2,"sita",78,3,"pooja",90]
for i in range(len(student)):
    if i%3==0:
        print(student[i])
for i in range(len(student)):
    if i%3==0:
        print(student[i+1])
for i in range(len(student)):
    if i%3==0:
        print(student[i+2])

#combine using one loop
student=[1,"ram",45,2,"sita",78,3,"pooja",90]
for i in range(len(student)):
    if i%3==0:
        print(student[i])
        print(student[i+1])
        print(student[i+2])
        print("==========")

#x=[101,57,6,98,32,57,98]
# 1)key check ex:98 (key found or not found)
# 2) duplicate element --> 5,7,9,8
# 3)unique element
# 4)without sorting-->sort
# 5)even element--> 0 odd element-->1
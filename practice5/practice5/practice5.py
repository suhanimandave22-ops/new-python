txt=input("Enter a string:")
count=0
for char in txt[::-1]:
    if char in "aeiou":
        count+=1
print("total ",count)
x = [101, 57, 6, 98, 32, 10, 57, 98]

#key found or not
print("\n1. Key Check")
key = 98
if key in x:
    print("Key Found")
else:
   print("Key Not Found")

#find duplicate
print("\n2. Duplicate Elements")
duplicates = []
for i in x:
    if x.count(i) > 1: 
        if i not in duplicates:
            duplicates.append(i)
print("Duplicates:", duplicates)

#unique
print("\n3. Unique Elements")
unique = []
for i in x:
    if x.count(i) == 1:
        unique.append(i)
print("Unique:", unique)


#even(0) and odd(1) element
print("\n4. Even (0), Odd (1)")
for i in x:
    if i%2==0:
        i=0
    else:
        i=1
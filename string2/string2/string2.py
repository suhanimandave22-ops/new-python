x="india is my country!"


# is
# count
# try !
# ym
# si
# s m
print(x[6:8])
print(x[12:17])
print(x[7:10])
print(x[16:])
print(x[-10:-15:-1])
print(x[::-1])
print(x[0:5])
print(x[:5])

#palindrome or not using string
ip=input("Enter string:")
if ip==ip[::-1]:
    print("palindrome")
else:
    print("not palindrome")

#count digit and char

x="abc1234"
ct_digit=0
ct_char=0
for i in x:
    if i.isdigit():
        ct_digit += 1
    elif i.isalpha():
        ct_char += 1

print("Digits:", ct_digit)
print("Characters:", ct_char)
#check ascii value of character
x="A"
print(ord(x))

print(ord('a'))
print(chr(97))
#a-->A

print(chr(ord('a')-32)) #a-z:97-122 A-z 65-90

print(chr(ord('C')+32))#C-c

x="hello"
new_str=""
for i in x:
    if i>='a' and i<='z':
        new_str+=chr(ord(i)-32)
print(new_str)

#sWapCase----->swapacase
x="sWapCase"
new=""
for i in x:
    if i>='a' and i<='z':
        new+=chr(ord(i)-32)
    elif i>='A' and i<='Z':
        new+=chr(ord(i)+32)
print(new)

#even char
x="programming"
for i in x:
    if ord(i)%2!=0:
        print(i,ord(i))


#HOMEWORK Question remove whitespace
x=" hi"
print(len(x))
new=""
for ch in x:
    if ch!=' ':
        new+=ch
print(new,len(new))

x="hello"
print('h' in x) #h==h
print('g' in x) #g==hello---->false

x=" hi"
print(len(x))
new=""
for ch in x:
    if ' ' not in ch:
        new+=ch
print("ans",new,len(new))

print(' ' not in ' ')
print(' ' not in 'i')

x="programming"
unique=""
for ch in x:
    if ch not in unique:
        unique+=ch
print(unique)

#practice own
x="i like python programming"
ct=x.count(' ')
ct+=1
print(ct)

x="i like python programming"
ct=1
for ch in x:
    if ' '==ch:
        ct+=1
print(ct)


# string programming 1.reverse string hello to olleh 2. check palindrome 3. convert slicing upper,lower,snaocase 4.count word of string 5.string char-->sort 

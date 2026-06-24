
a="Maharashtra"
even=a[::2]
print("Even character:",even)
odd=a[1::2]
print("Odd character:",odd)
print("vowels:",end=" ")
for ch in a:
    if ch in "aeiou":
        print(ch,end="")
print()

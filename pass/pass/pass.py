pwd=input("Enter a password:")
if len(pwd)>=3 and len(pwd)<=6:
    print("weak pwd")
elif len(pwd)>=6 and len(pwd)<=8:
    print("Strong pwd")
elif len(pwd)>=8 and len(pwd)<=20:
    print("Very strong pwd")
else:
    print("invalid")


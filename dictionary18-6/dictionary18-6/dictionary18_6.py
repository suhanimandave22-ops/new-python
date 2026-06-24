'''stud={
    "rollno":101,
    "name":"Ram",
    "age":30,
    "sub":["math","eng"],
    "marks":(90,89,67)
    }
print(stud)
#loop
for values in stud.values():
    print(values)

for k,v in stud.items():
    print(k,v)

#methods
print(stud.keys())
print(stud.values())

us="sub"
print(stud["age"])
print(stud["sub"][1])
print(stud["marks"][2])

for k,v in stud.items():
    print(k,v)

print(len(stud["sub"]))
for i in range(len(stud["sub"])):
    print(f"{stud["sub"][i]}:{stud["marks"][i]}")

#zip()
for sv,mv in zip(stud["sub"],stud["marks"]):
    print(sv,mv)

stud={
    101:{
    "name":"Ram",
    "age":30,
    "sub":["math","eng"],
    "marks":(90,67)
    },
    102:{
    "name":"sita",
    "age":23,
    "sub":["math","eng"],
    "marks":(90,89)
    },
    103:{
    "name":"shyam",
    "age":24,
    "sub":["math","eng"],
    "marks":(89,67)
    }
}
print(stud[101]["sub"][1])

for key in stud.values():
    print()

for key in stud:
    for v in stud[key]["marks"]:
        print(v, end=" ")
    print()


for key.details in stud.items():
    print("Student id:{key}")

1) add student according user
2) each student total marks and calculate percentage
3) each subject topper in according subjecct and also lowest using choice basis '''

# grocery={ "grocery"}:{"spices":{type:masala mfg:today,expiry:after 5 days,price:200rs,netgrm:10 brand:suhani }},{"biscuit"}:{store entire info}

student={
    "name": "suhani",
    "age": 21,
    "course": "python"}
print(student)
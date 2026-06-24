autoperkm = 15
cabperkm = 25
print("1.auto \n2.Cab")
print("-----------------------------------------")
ch = int(input("Enter your choice:"))
print("-----------------------------------------")
if ch == 1:
    distance = float(input("Enter distance in kilometers: "))
    auto = distance * autoperkm
    print("Auto")
    print("Distance:", distance, "km")
    print("Price per km:", autoperkm)
    print("Total price:", auto)

elif ch == 2:
    distance = float(input("Enter distance in kilometers: "))
    cab = distance * cabperkm
    print("Cab")
    print("Distance:", distance, "km")
    print("Price per km:", cabperkm)
    print("Total price:", cab)

else:
    print("Invalid choice!")

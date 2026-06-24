autoperkm=15
cabperkm=25
print("1.auto \n2.Cab")
print("-----------------------------------")
ch=int(input("Enter your choice:"))
print("-----------------------------------")
match ch:
    case 1:
        distance = float(input("Enter distance in kilometers: "))
        print("-----------------------------------")
        auto = distance * autoperkm
        print("Auto")
        print("Distance:", distance, "km")
        print("Price per km:", autoperkm)
        print("Total price:", auto)

    case 2:
        distance =float(input("Enter distance in kilometers:"))
        print("-----------------------------------")
        cab=distance*cabperkm
        print("Cab")
        print("Distance:",distance, "km")
        print("Price per km:", cabperkm)
        print("Total price:", cab)

    case 3:
        print("Invalid choice!")
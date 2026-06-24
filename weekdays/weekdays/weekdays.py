day=int(input("Enter day to check between(1-7):"))
match day:
    case 1 | 2 | 3 | 4 | 5:
        print("Weekday")
    case 6 | 7:
        print("weekend")
    case _:
        print("Invalid choice")


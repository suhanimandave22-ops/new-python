print("GEO calci\n1.Rectangle.\n2.Triangle.\n3.Circle.\n4.Exit")
choice = int(input("Enter your choice: "))
match choice:
    case 1:
        print("Rectangle case executed!")
        print("1.Area.\n2.Perimeter.\n3.Exit")
        ip = int(input("Enter your choice: "))

        match ip:
            case 1:
                length = float(input("Enter length: "))
                breadth = float(input("Enter breadth: "))
                area = length * breadth
                print("Area of rectangle is", area)

            case 2:
                length = float(input("Enter length: "))
                breadth = float(input("Enter breadth: "))
                perimeter = 2 * (length + breadth)
                print("Perimeter of rectangle is", perimeter)

            case 3:
                print("Exit from rectangle")

            case _:
                print("Invalid choice of rectangle operation")

    case 2:
        print("Triangle case executed!")
        print("1.Area.\n2.Side.\n3.Exit")
        ip = int(input("Enter your choice: "))

        match ip:
            case 1:
                base = float(input("Enter base: "))
                height = float(input("Enter height: "))
                area = 0.5 * base * height
                print("Area of triangle is", area)

            case 2:
                side = float(input("Enter side: "))
                print("Side of triangle is", side)

            case 3:
                print("Exit from triangle")

            case _:
                print("Invalid choice of a triangle operation")

    case 3:
        print("Circle case executed!")
        radius = float(input("Enter radius: "))
        area = 3.14 * radius * radius
        print("Area of circle is", area)

    case 4:
        print("Thank You")

    case _:
        print("Invalid choice")
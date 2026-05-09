seat_type = input("Enter your Seat Type (sleeper/AC/general/luxury: )").lower()

match seat_type:
    case "sleeper":
        print("U can Actullay sleep there");
    case "ac":
        print("U will get AC to sit");
    case "general":
        print("U dont't get much facility");
    case "luxury":
        print("Maje hi Maje");
    case _:
        print("We Don't get what u are asking for")
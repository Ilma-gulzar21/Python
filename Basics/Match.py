day = input("Enter Any color of Traffic = ")

match day:
    case "Green":
        print("Go")

    case "Yellow":
       print("Look")

    case "Red":
      print("Stop")
    case  _:
      print("invalid")
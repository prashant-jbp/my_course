# 1 . its monday
# 2 . its  tuseday

# _ : invalid input
# find day by its given number
day = input("Enter a day number = ")
match day:
    case "mon": print("Its Monday 1 day")
    case "tue": print("Its Tuesday")
    case "wed": print("Its wednesday")
    case "thu": print("Its Thursday")
    case "fri": print("Its Friday")
    case "sat": print("Its Saturday")
    case "sun": print("Its Sunday")
    case _: print("Invalid Input")

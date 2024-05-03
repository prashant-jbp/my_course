# 1 . its monday
# 2 . its  tuseday

# _ : invalid input
# find day by its given number
day = int(input("Enter a day number = "))
match day:
    case 1: print("Its Monday")
    case 2: print("Its Tuesday")
    case 3: print("Its wednesday")
    case 4: print("Its Thursday")
    case 5: print("Its Friday")
    case 6: print("Its Saturday")
    case 7: print("Its Sunday")
    case _: print("Invalid Input")

dayWeek = ["This day does not exist. Please, try again...", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
day = int(input("Enter the day of the week: "))
if day == 0:
    print("%s" % dayWeek[day])
elif day > 7:
    print("%s" % dayWeek[0])
    exit(0)
while True:
    match day:
        case 1:
            print("Today is %s." % dayWeek[day])
            break
        case 2:
            print("Today is %s." % dayWeek[day])
            break
        case 3:
            print("Today is %s." % dayWeek[day])
            break
        case 4:
            print("Today is %s." % dayWeek[day])
            break
        case 5:
            print("Today is %s." % dayWeek[day])
            break
        case 6:
            print("Today is %s." % dayWeek[day])
            break
        case 7:
            print("Today is %s." % dayWeek[day])
            break
    exit(0)

def number_value():
    num = int(input("Enter a number: "))

    if num == 0:
        print("This is zero.")
    elif num > 0:
        print("This is a positive number.")
    elif num < 0:
        print("This is a negative number.")
    else:
        print("Error: Invalid input!")

number_value()
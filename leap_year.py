def leap_year():
    year = int(input("Enter a year: "))

    if year % 4 == 0:
        print(f"{year} is a leap year.")
    elif year < 1:
        print("Error: Invalid Input!")
    else:
        print(f"{year} is not a leap year.")

leap_year()
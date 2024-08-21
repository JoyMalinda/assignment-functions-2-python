def insurance_check():
    age = int(input("How old are you? "))
    
    marr1 = input("Are you married [y/n]? ")
    marr2 = marr1.lower()

    gender1 = input("Are you male or female[m/f]? ")
    gender2 = gender1.lower()

    if marr2 not in ["yes", "y", "no", "n"]:
        print("Error: Invalid Input for Marriage Status!")
    elif gender2 not in ["male", "m", "female", "f"]:
        print ("Error: Invalid Input for Gender!")
    elif marr2 == "yes" or marr2 == "y":
        print("Congratulations! You are insured!")
    elif marr2 in ["no", "n"] and gender2 in ["male", "m"] and age > 30:
        print("Congratulations! You are insured!")
    elif marr2 in ["no", "n"]and gender2 in ["female", "f"] and age > 25:
        print("Congratulations! You are insured!")
    else:
        print("Sorry! You are not insured!")

insurance_check()

    
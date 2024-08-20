def character_value():
    letter = input("Enter a letter: ")
    letter1 = letter.lower()

    if not letter1.isalpha() or len(letter1) != 1:
        print("Invalid Input: Please enter a single letter.")
    elif letter1 == "a" or letter1 == "e" or letter1 == "i" or letter1 == "o" or letter1 == "u":
        print(f"{letter1} is a vowel.")
    else:
        print(f"{letter1} is a consonant.")

character_value()
def student_grading():
    marks = int(input("Enter the student's marks: "))

    if marks < 0 or marks > 100:
        print("Error: Invalid input!")
    elif marks <= 100 and marks >= 90:
        print("Excellent Performance!")
    elif marks >= 80 and marks < 90:
        print("Ver Good Performace!")
    elif marks >= 70 and marks < 80:
        print("Good Performance!")
    elif marks >= 60 and marks < 70:
        print("Average Performance!")
    else:
        print("Poor Performance!")

student_grading()
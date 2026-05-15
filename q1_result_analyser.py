def analyze_result(name, roll, marks):
    print("name = ", name)
    print("roll = ", roll)
    print("marks = ", marks)

    total = sum(marks)
    avg = total / len(marks)

    print("Total = ", total)
    print("Average = ", avg)

    if avg >= 90:
        Grade = 'A'
    elif avg >= 75:
        Grade = 'B'
    elif avg >= 60:
        Grade = 'C'
    elif avg >= 40:
        Grade = 'D'
    else:
        Grade = 'Fail'
    print("Grade: ",Grade)
    
    for i in range(len(marks)):
        if marks[i] < 40:
            print("Subjects below 40: Subject", i + 1)


# MAIN PROGRAM
name = input("name = ")
roll = int(input("roll = "))

marks = []
marks.append(88.5)
marks.append(35.0)
marks.append(76.0)
marks.append(92.5)
marks.append(48.0)

analyze_result(name, roll, marks)
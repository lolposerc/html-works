def StudentGrades():
    grades = []

    for index in range(0,5):
        print("="*40)
        grade = float(input(f"Введите {index+1} оценку:"))
        grades.append(grade)
    
    print("="*40)
    print(f"Оценки: {grades}")

    for grade in grades:
        if grade > 100 and grade < 100:
            print(f"тудент не может сдать на оценку: '{grade}' (0-100)")
            return
    
    MiddleGrade = sum(grades) / len(grades)
    print("="*40)
    print(f"Средняя оценка: {MiddleGrade}")
    print("")
    if MiddleGrade >= 90:
        print("Студент сдал на отлично!")
    elif MiddleGrade >= 80 and MiddleGrade <= 89:
        print("Студент сдал на хорошо!")
    elif MiddleGrade >= 70 and MiddleGrade <= 79:
        print("Студент сдал на удовлетворительно!")
    elif MiddleGrade >= 60 and MiddleGrade <= 69:
        print("Студент сдал на ниже среднего!")
    elif MiddleGrade <= 59:
        print("Студент сдал на неудовлетворительно!")
    print("")
    if MiddleGrade >= 79:
        print("Студент сдал!")
    else:
        print("Студент не сдал!")
    print("")
    print(f"Самая низкая оценка: {min(grades)}, Самая высокая: {max(grades)}")
    print("="*40)
StudentGrades()
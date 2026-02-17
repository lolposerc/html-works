student1 = ("Иван", "Иванов", 85, 92)
student2 = ("Мария", "Петрова", 78, 88)
student3 = ("Алексей", "Сидоров", 95, 90)

Students = (student1,student2,student3)

SmartStudent = [0,""]

for student in Students:
    print()
    print("="*40)
    print()

    name, surname, math, physics = student

    print(f"Имя: {name}")
    print(f"Фамилия: {surname}")

    MiddleGrade = (math + physics) / 2

    if MiddleGrade > SmartStudent[0]:
        SmartStudent[0] = MiddleGrade
        SmartStudent[1] = name

    if math >= 60 and physics >= 60:
        print(f"Сдал(a) все предметы")
    else:
        print(f"Не cдал(a) все предметы")
    
    print(f"Средняя оценка: {MiddleGrade}")

print()
print("="*40)
print()

print(f"Студент {SmartStudent[1]}, с самым высоким средним балом '{SmartStudent[0]}'")

print()
print("="*40)
print()
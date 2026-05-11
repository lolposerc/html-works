import datetime


def save_to_file(date, mood, description):
    with open("mood_diary.txt", "a", encoding="utf-8") as file:
        if description == "":
            description = "Нет"
        file.write(f"[{date}] Настроение: {mood}\nОписание: {description}\n")
    print("Запись сохранена!\n")

def show_weekly_stats():
    lines = None
    try:
        with open("mood_diary.txt", "r", encoding="utf-8") as file:
            lines = file.readlines()
    except FileNotFoundError:
        print("Файл с записями не найден.")
        return

    today = datetime.date.today()
    one_week_ago = today - datetime.timedelta(days=7)
    mood_scores = []
    happiest_day = None
    max_mood = 0

    i = 0
    while True:
        if i >= len(lines):
            break
        line = lines[i]
        date_str = ""
        is_mood = False
        for char in line:
            if char == "[":
                is_mood = True
            elif char == "]":
                is_mood = False
            else:
                if is_mood == True:
                    date_str = f"{date_str}{char}"
        # print(date_str)
        try:
            date = datetime.datetime.strptime(date_str, "%Y-%m-%d").date()
            
            if date >= one_week_ago:
                try:
                    mood_part = line.split("Настроение: ")[1].split()[0]
                    mood_score = int(mood_part)
                    mood_scores.append(mood_score)

                    if mood_score > max_mood:
                        max_mood = mood_score
                        happiest_day = date_str
                except ValueError:
                    pass
        except ValueError:
            pass
        i += 1

    if mood_scores:
        average_mood = sum(mood_scores) / len(mood_scores)
        print("Статистика за неделю:")
        print(f"Среднее настроение: {average_mood}")
        if happiest_day:
            print(f"Самый счастливый день: {happiest_day} ({max_mood}/5)")
    else:
        print("За последнюю неделю записей нет.")

print("=== ДНЕВНИК НАСТРОЕНИЯ ===")

date = None
mood = 1
description = ""

date_input = input("Введите дату (Enter для сегодня): ")

if not date_input:
    date = datetime.date.today().strftime("%Y-%m-%d")
else:
    date = date_input

while True:
    try:
        mood = int(input("Настроение (1-5): "))
        if 1 <= mood and 5 >= mood:
            break
        else:
            print("Пожалуйста, введите число от 1 до 5")
    except ValueError:
        print("Пожалуйста, введите число от 1 до 5")

description = input("Опишите день: ")



save_to_file(date, mood, description)

show_weekly_stats()

    

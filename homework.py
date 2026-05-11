import random
import time

stats = []

def show_statistics():
    gamecount = 0
    for stat in stats:
        print("-"*40)
        print(f"Игра: {len(stats) - (len(stats)-gamecount) + 1}")
        gamecount += 1
        print(f'    Очки за игру: {stat["score"]}')
        print(f'    Время за игру: {stat["time"]}')
        print(f'    Попыток за игру: {stat["attempts"]}')
        print("-"*40)

def generate_hint(secret, guess):
    if secret == guess:
        print("="*40)
        print()
        print("Вы угадали число!")

        return True

    value = abs(secret - guess)

    if value <= 5:
        print("Горячо!")
    elif value <= 15:
        print("Тепло")
    else:
        print("Холодно")
    
    if secret < guess:
        print("Загаданное число: Меньше")
    else:
        print("Загаданное число: Больше")

    return False

def save_stats(score,gameTime,attempts):
    data = {
        "score": score,
        "time": gameTime,
        "attempts": attempts
    }
    stats.append(data)

def calculate_score(attempts, gameTime):
    score = 100 - attempts * 10
    currentTime = time.time()
    newTime = 10 - (currentTime - gameTime)
    print()
    print(f"Очков за количество попыток: {score}")
    print()

    if newTime >= 0:
        print(f"+ Очков за быстрое время: {int(newTime)}")
        print()
        score += int(newTime)

    if score <= 0:
        score = 0
    
    print(f"Всего очков: {score}")
    print()
    print("="*40)

    save_stats(score,int(newTime),attempts)
def play_game():
    secretNumber = random.randint(1,100)
    startGameTimer = time.time()
    attempts = 0

    print(secretNumber)

    while True:
        
        try:
            guess = int(input("Введите число от 1-100: "))
            attempts += 1

            hint = generate_hint(secretNumber, guess)

            if hint == True:
                calculate_score(attempts, startGameTimer)
                break
        except ValueError :
            print("Пожалуйста введите число.")

while True:
    try:
        print("Игра: 'УГАДАЙ ЧИСЛО!'")
        print("    1. играть")
        print("    2. статистика")
        choice = int(input("Выберите вариант: "))
        print()
        if choice < 1 or choice > 2:
            print(f"Не существует варианта: {choice}")
            print("Попробуйте снова.")
            print()
        elif choice == 1:
            play_game()
        elif choice == 2:
            show_statistics()
    except ValueError:
        print()
        print("Ошибка при вводе варианта. Попробуйте снова.")
        print()

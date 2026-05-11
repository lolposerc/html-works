players = {
    1: {"name": "Алексей", "rating": 1000, "matches": 0},
    2: {"name": "Мария", "rating": 1000, "matches": 0},
    3: {"name": "Дмитрий", "rating": 1000, "matches": 0}
}

def get_rating_delta(rating_a, rating_b, result):
    # (Change): Change = K * (Результат - E)
    # (E): E = 1 / (1 + 10 ** ((Рейтинг_соперника - Рейтинг_игрока) / 400))
    # Новый_рейтинг = Старый_рейтинг + Change

    

    if result == 1 or result == 0.5:
        pass
    else:
        result = 0

    E = 1 / (1 + 10 ** ((rating_b - rating_a) / 400))
    Change = 32 * (result - E)
    NewRatingA = rating_a + Change

    return round(NewRatingA)

# print(get_rating_delta(players[1]["rating"],players[2]["rating"],1))

def register_match(p1_id, p2_id, winner):
    if winner == 1 or winner == 2:
        pass
    else:
        winner = 0
    
    player1 = players[p1_id]
    player2 = players[p2_id]

    player1["matches"] += 1
    player2["matches"] += 1

    if winner == 0:
        print(f"Матч закончился ничьй для '{player1["name"]}' и '{player2["name"]}'")
    else:
        playerWin = player1["name"]
        player1Won = 1
        player2Won = 0

        if winner == 2:
            playerWin = player2["name"]
            player1Won = 0
            player1Won = 1
        
        player1Rating = get_rating_delta(player1["rating"], player2["rating"], player1Won)
        player2Rating = get_rating_delta(player2["rating"], player1["rating"], player2Won)
    
        print(f"Выиграл игрок: '{playerWin}'")

        player1["rating"] = player1Rating
        player2["rating"] = player2Rating

def show_leaderboard():
    print(f"Лидерборд:")
    for id in players:
        data = players[id]
        name = data["name"]
        rating = data["rating"]
        matches = data["matches"]
        print("="*40)
        print(f" Имя: {name}")
        print("---------Информация---------")
        print(f"    Рейтинг: {rating}")
        print(f"    Сыгранно матчей: {matches}")
        print("-"*28)
    print("="*40)
    

    

print()

register_match(3, 1, 2)

print()

register_match(2, 3, 1)

print()

register_match(2, 1, 0)

print()

register_match(3, 1, 1)

print()

show_leaderboard()




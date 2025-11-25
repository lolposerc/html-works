let hunger = 50;
let happiness = 50;
let health = 50;

let inGame = true

while (inGame == true) {
    let action = prompt(`
        Ваш питомец:
        Голод: ${hunger}
        Счастье: ${happiness}
        Здоровье: ${health}
        ---
        Чем займемся?
        1. Кормить
        2. Играть
        3. Уложить спать
        4. Выход
    `);

    switch (action) {
        case '1':
            hunger += 5;
            happiness -= 1;
            health -= 1
            break
        case '2':
            hunger -= 5;
            happiness += 15;
            health -= 5
            break
        case '3':
            hunger -= 10;
            happiness -= 3;
            health = 100
            break
        case '4':
            inGame = false
    }

    if (hunger >= 100, happiness <= 0, health <= 0) {
        inGame = false
    }
}

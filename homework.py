from datetime import datetime

BOOKS_FILE = "books.txt"
STATUS_AVAILABLE = "доступна"
STATUS_GIVEN = "выдана"

def load_books():
    books = []
    try:
        with open(BOOKS_FILE, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line:
                    parts = line.split(";")
                    books.append({
                        "title": parts[0],
                        "author": parts[1],
                        "year": int(parts[2]),
                        "genre": parts[3],
                        "status": parts[4]
                    })
                print(f'Было загружено книг: {len(books)}')
    except FileNotFoundError:
        print('Ошибка при обноружении книг')
    return books

def save_books(books):
    with open(BOOKS_FILE, "w", encoding="utf-8") as f:
        for book in books:
            f.write(f"{book['title']};{book['author']};{book['year']};{book['genre']};{book['status']}\n")

def show_all_books():
    print("=== ВСЕ КНИГИ В БИБЛИОТЕКЕ ===")
    books = load_books()
    if not books:
        print("Библиотека пуста.")
        return

    for i, book in enumerate(books, 1):
        status_icon = "✅" if book["status"] == STATUS_AVAILABLE else "🔄"
        print(f"{i}. {book['title']} | {book['author']} ({book['year']}) [{book['genre']}] - {status_icon} {book['status']}")

    available_count = sum(1 for b in books if b["status"] == STATUS_AVAILABLE)
    given_count = len(books) - available_count
    print(f"Всего книг: {len(books)} (доступно: {available_count}, выдано: {given_count})")

def add_book():
    print("=== ДОБАВЛЕНИЕ НОВОЙ КНИГИ ===")
    title = input("Введите название: ").strip()
    author = input("Введите автора: ").strip()
    year_str = input("Введите год: ").strip()
    genre = input("Введите жанр: ").strip()

    if not year_str.isdigit():
        print("Ошибка: год должен быть числом.")
        return
    year = int(year_str)
    current_year = datetime.now().year
    if year < 1000 or year > current_year:
        print(f"Ошибка: год должен быть от 1000 до {current_year}.")
        return

    books = load_books()
    books.append({
        "title": title,
        "author": author,
        "year": year,
        "genre": genre,
        "status": STATUS_AVAILABLE
    })
    save_books(books)
    print("✅ Книга успешно добавлена!")

def find_books():
    print("=== ПОИСК КНИГИ ===")
    print("Искать по:")
    print("1. Названию")
    print("2. Автору")
    print("3. Жанру")
    print("4. Вернуться")
    choice = input("Выбор: ").strip()

    if choice == "4":
        return

    if choice not in ["1", "2", "3"]:
        print("Неверный выбор.")
        return

    query = input("Введите запрос: ").strip().lower()
    books = load_books()
    found = []

    for book in books:
        if choice == "1" and query in book["title"].lower():
            found.append(book)
        elif choice == "2" and query in book["author"].lower():
            found.append(book)
        elif choice == "3" and query in book["genre"].lower():
            found.append(book)

    if found:
        print(f"Найдено {len(found)} книга:")
        for book in found:
            status_icon = "✅" if book["status"] == STATUS_AVAILABLE else "🔄"
            print(f"- {book['title']} | {book['author']} ({book['year']}) [{book['genre']}] - {status_icon} {book['status']}")
    else:
        print("Книг не найдено.")

def manage_book_status():
    print("=== ВЫДАЧА/ВОЗВРАТ КНИГИ ===")
    books = load_books()
    available_books = [b for b in books if b["status"] == STATUS_AVAILABLE]

    if not available_books:
        print("Нет доступных для выдачи книг.")
        return

    print("Доступные книги:")
    for i, book in enumerate(available_books, 1):
        print(f"{i}. {book['title']} | {book['author']} ({book['year']}) [{book['genre']}]")

    try:
        book_num = int(input("Выберите номер книги: ")) - 1
        if book_num < 0 or book_num >= len(available_books):
            print("Неверный номер.")
            return
    except ValueError:
        print("Введите число.")
        return

    selected_book = available_books[book_num]

    print("Действие:")
    print("1. Выдать книгу")
    print("2. Вернуть книгу")
    action = input("Выбор: ").strip()

    if action == "1":
        reader = input("Введите имя читателя: ").strip()
        selected_book["status"] = STATUS_GIVEN
        print(f"✅ Книга \"{selected_book['title']}\" выдана {reader}")
    elif action == "2":
        selected_book["status"] = STATUS_AVAILABLE
        print(f"✅ Книга \"{selected_book['title']}\" возвращена")
    else:
        print("Неверное действие.")
        return

    for b in books:
        if b["title"] == selected_book["title"] and b["author"] == selected_book["author"]:
            b["status"] = selected_book["status"]
            break

    save_books(books)

def show_stats():
    print("=== СТАТИСТИКА БИБЛИОТЕКИ ===")
    books = load_books()
    total = len(books)
    if total == 0:
        print("Библиотека пуста.")
        return

    available_count = sum(1 for b in books if b["status"] == STATUS_AVAILABLE)
    given_count = total - available_count

    print("📈 Общая статистика:")
    print(f"Всего книг: {total}")
    print(f"Доступно сейчас: {available_count} ({available_count / total * 100:.0f}%)")
    print(f"Выдано: {given_count} ({given_count / total * 100:.0f}%)")

    genre_count = {}
    for book in books:
        genre = book["genre"]
        genre_count[genre] = genre_count.get(genre, 0) + 1

    sorted_genres = sorted(genre_count.items(), key=lambda x: x[1], reverse=True)
    print("🏆 Топ-3 жанра:")
    for i, (genre, count) in enumerate(sorted_genres[:3], 1):
        print(f"{i}. {genre}: {count} книг")

    oldest_year = min(book["year"] for book in books)
    print(f"📅 Самый старый год издания: {oldest_year}")

def show_main_menu():
    print("\n" + "="*40)
    print("📚 МИНИ-БИБЛИОТЕКА")
    print("="*40)
    print("1. 📖 Показать все книги")
    print("2. ➕ Добавить книгу")
    print("3. 🔍 Найти книгу")
    print("4. 🔄 Выдать/вернуть книгу")
    print("5. 📊 Статистика")
    print("6. ❌ Выход")
    print("="*40)
    choice = input("Выберите действие (1-6): ")
    return choice


while True:
    choice = show_main_menu()

    if choice == "1":
        show_all_books()
    elif choice == "2":
        add_book()
    elif choice == "3":
        find_books()
    elif choice == "4":
        manage_book_status()
    elif choice == "5":
        show_stats()
    elif choice == "6":
        print("="*40)
        print("Вы вышли из библиоттеки")
        print("="*40)
        break
    else:
        print("Пожалуйста, выберите действие от 1 до 6")


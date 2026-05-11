def total_revenue(sales):
    result = 0
    for data in sales:
        result += data["price"]
    return result

def best_selling_product(sales):
    result = {"price":0}
    for data in sales:
        if data.get("price") > result.get("price"):
            result = data.copy()
    result = result["product"]
    return result

def best_seller(sales):
    result = {"price":0}
    for data in sales:
        if data.get("price") > result.get("price"):
            result = data.copy()
    result = result["seller"]
    return result

def sales_by_category(sales):
    result = {}
    for data in sales:
        category = data.get("category")
        if result.get(category) == None:
            result[category] = data.get("price") or 0
        else:
            result[category] += data.get("price") or 0
    return result

def daily_sales(sales):
    result = {}
    for data in sales:
        date = data.get("date")
        if result.get(date) == None:
            result[date] = data.get("price") or 0
        else:
            result[date] += data.get("price") or 0
    return result

def add_sale(sales, new_sale):
    data_check = [
        "date",
        "product",
        "category",
        "price",
        "quantity",
        "seller",
    ]

    not_find = None

    for data in data_check:
        if new_sale.get(data) == None:
            not_find = data
            break
    
    if not_find != None:
        print(f"Ошибка в добавлении товара! В продукте не было обнаружено параметр: '{not_find}'")
    else:
        sales.append(new_sale)
        print(f"Товар {new_sale.get("product")} успешно добавлен!")

    return sales

def split_date(date):
    if date != None:
        word = ""
        for char in date:
            if char == "-":
                char = " "
            word = f"{word}{char}"
        split_date = word.split()
        return split_date

def calculate_date(date, start_date, end_date):
    year,num,month = split_date(date)
    start_year,start_num,start_month = split_date(start_date)
    end_year,end_num,end_month = split_date(end_date)

    if start_year <= year and year <= end_year and start_num <= num and num <= end_num and start_month <= month and year <= end_month:
        return True    

        
def generate_report(sales, start_date, end_date):
    reports = []

    print("="*40)

    print()
    print(f"Отчёт за период: от {start_date} до {end_date}")
    print()

    for sale in sales:
        if calculate_date(sale.get("date"), start_date, end_date) == True:
            reports.append(sale.get("date"))
    
    print(f"Общая выручка: {total_revenue(sales)} руб.")

    print()

    print(f"Лучший товар: {best_selling_product(sales)}")

    print()

    print(f"Лучший продавец: {best_seller(sales)}")

    print()

    print(f"Выручка по категориям: {sales_by_category(sales)}")

    print()

    print(f"Выручка по дням: {daily_sales(sales)}")

# Тестовые данные
sales = [
    {'date': '2024-01-01', 'product': 'Ноутбук', 'category': 'Электроника', 
     'price': 75000, 'quantity': 2, 'seller': 'Иванов'},
    {'date': '2024-01-02', 'product': 'Мышь', 'category': 'Электроника', 
     'price': 1500, 'quantity': 5, 'seller': 'Петров'},
    {'date': '2024-01-02', 'product': 'Лего', 'category': 'Игрушки', 
     'price': 1300, 'quantity': 25, 'seller': 'Алексей'},
    {'date': '2024-01-03', 'product': 'Планшет', 'category': 'Электроника', 
     'price': 12000, 'quantity': 3, 'seller': 'Иванов'},
]

print(f"Общая выручка: {total_revenue(sales)} руб.")

print()

print(f"Лучший товар: {best_selling_product(sales)}")

print()

print(f"Лучший продавец: {best_seller(sales)}")

print()

print(f"Выручка по категориям: {sales_by_category(sales)}")

print()

print(f"Выручка по дням: {daily_sales(sales)}")

print()

sales = add_sale(sales,{'product': 'Микрофон', 'category': 'Электроника', 'price': 5000, 'quantity': 3, 'seller': 'Алексей'})

print()

sales = add_sale(sales,{'date': '2024-01-03', 'product': 'Клавиатура', 'category': 'Электроника', 'price': 2000, 'quantity': 1, 'seller': 'Петров'})

print()

generate_report(sales, "2024-01-01", "2024-01-03")



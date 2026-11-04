from db import connect_db

# 09 Товары по бюджету 
# 1. Запросите целый неотрицательный бюджет. 
# 2. Покажите товары не дороже бюджета и только с положительным остатком. 
# 3. Отсортируйте по возрастанию цены, при одинаковой цене — по ID. Для пустого ответа покажите сообщение.

def read_int(variable, minimum):
    while True:
        text = input(variable)
        try:
            value = int(text)
        except ValueError:
            print("Введите целое число!")
            continue
        if value < minimum:
            print(f"Минимум: {minimum}")
            continue
        return value

def show_budget():
    limit = read_int("Ваш бюджет: ", 1)
    sql = """
        SELECT id, name, price, stock
        FROM terminal_products
        WHERE price <= %s AND stock > 0
        ORDER BY price, id;
    """
    with connect_db() as conn:
        with conn.cursor() as cur:
            cur.execute(sql, (limit,))
            rows = cur.fetchall()
    
    for row in rows:
        print(row["id"], row["name"], row["price"], row["stock"])
        
show_budget()
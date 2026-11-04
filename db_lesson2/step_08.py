from db import connect_db
import psycopg 

# 08 Свой товар в каталоге 
# 1. Добавьте товар с новым положительным ID, непустым названием, положительной ценой и неотрицательным остатком. 
# 2. Проверьте ID 99, название Веб камера, цену 12000, остаток 1. 
# 3. При повторе ID сообщите, что номер занят. Проверьте, что исходные товары сохранились.

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
    
def add_product():
    product_id = read_int("Новый ID: ", 1)
    name = input("Новое имя: ").strip()
    if not name:
        print("Название не должно быть пустым!")
        return
    price = read_int("Новая цена: ", 1)
    stock = read_int("Новое наличие: ", 0)
    
    sql = """
        INSERT INTO terminal_products (id, name, price, stock)
        VALUES (%s, %s, %s, %s);
    """
    try:
        with connect_db() as conn:
            with conn.cursor() as cur:
                cur.execute(sql, (product_id, name, price, stock))
    except psycopg.UniqueViolation:
        print("Этот ID уже занят!")
        return
    print("Товар добавлен!")
    
add_product()
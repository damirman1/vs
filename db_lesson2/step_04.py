from db import connect_db

# 04 Карточка по номеру 
# 1. Запросите положительный целый ID товара. 
# 2. Найдите и покажите его название, цену и остаток. 
# 3. Для отсутствующего ID выведите Товар не найден. Проверьте ввод букв и нуля. 

def read_int(variable, minimum):
    while True:
        text = input(variable)
        try:
            value = int(text)
        except ValueError:
            print("Введите целое число!")
            continue
        if value < minimum:
            print(f"Минимальное значение: {minimum}")
            continue
        return value

def find_product():
    product_id = read_int("ID товара: ", 1)
    sql = """
        SELECT id, name, price, stock 
        FROM terminal_products
        WHERE id = %s;
    """
    
    with connect_db() as conn:
        with conn.cursor() as cur:
            cur.execute(sql, (product_id,))
            row = cur.fetchone()
    
    if row is None:
        print("Товар не найден!")
    else:
        print(row["name"], row["price"], row["stock"])
        
find_product()
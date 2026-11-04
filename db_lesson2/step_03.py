from db import connect_db

# 03 Каталог в терминале 
# 1. Покажите все товары в порядке ID. 
# 2. Выведите номер, название, цену в тенге и остаток. 
# 3. Если каталог пуст, покажите понятное сообщение. Запустите step_03.py. 

sql = """
SELECT id, name, price, stock 
FROM terminal_products ORDER BY id;
"""

def show_products():
    sql = """
        SELECT id, name, price, stock 
        FROM terminal_products ORDER BY id;
    """
    with connect_db() as conn:
        with conn.cursor() as cur:
            cur.execute(sql)
            rows = cur.fetchall()
    
    if not rows:
        print("Каталог пустой!")
    
    for row in rows:
        print(row["id"], row["name"], row["price"], row["stock"])
        
show_products()


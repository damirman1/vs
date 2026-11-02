from db import connect_db

# 03 Экран без лишних полей 
# 1. Создайте task_03.py. Получите только cargo и price. 
# 2. Сохраните порядок по id. Сам id печатать не нужно. 
# 3. Выведите груз и стоимость через print, обращаясь к ключам словаря.

sql = """
SELECT cargo, price
FROM lesson_deliveries
ORDER BY id;
"""
with connect_db() as conn:
    with conn.cursor() as cur:
        cur.execute(sql)
        rows = cur.fetchall()
        
    for row in rows:
        print(row["cargo"], row["price"])
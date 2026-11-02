# 05 Доставки от заданной стоимости 
# 1. Создайте task_05.py. Покажите доставки со стоимостью не ниже 1500 тг. 
# 2. Выведите cargo и price с порядком по id. Статус на отбор не влияет. 
# 3. Проверьте, что доставка ровно за 1500 тоже показана. 

from db import connect_db

sql = """
SELECT cargo, price
FROM lesson_deliveries
WHERE price >= 1500
ORDER BY id;
"""

with connect_db() as conn:
    with conn.cursor() as cur:
        cur.execute(sql)
        rows = cur.fetchall()
        
    for row in rows:
        print(row["cargo"], row["price"])
        
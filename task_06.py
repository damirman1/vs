# 06 Самая дорогая доставка первой 
# 1. Создайте task_06.py. Получите все грузы и их стоимость. 
# 2. Расположите строки по убыванию price, без фильтра по статусу. 
# 3. Выведите все пять строк.

from db import connect_db

sql = """
SELECT cargo, price
FROM lesson_deliveries
ORDER BY price DESC;
"""

with connect_db() as conn:
    with conn.cursor() as cur:
        cur.execute(sql)
        rows = cur.fetchall()
        
    for row in rows:
        print(row["cargo"], row["price"])
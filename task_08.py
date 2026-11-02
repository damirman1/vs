# 08 Новая срочная посылка 
# 1. Создайте task_08.py. Добавьте одну тестовую доставку: id 99, груз Медикаменты, стоимость 1800, статус ready. 
# 2. Задайте значения переменными и передайте их параметрами SQL. 
# 3. После успешного завершения выведите число добавленных строк. Проверьте запись через SELECT по id 99. Вставку выполняйте только одним способом и один раз. 

from db import connect_db

delivery_id = 99
cargo = "Медикаменты"
price = 1800
status = "ready"

sql = """
INSERT INTO lesson_deliveries (id, cargo, price, status) 
VALUES (%s, %s, %s, %s)
"""

with connect_db() as conn:
    with conn.cursor() as cur:
        cur.execute(sql, (delivery_id, cargo, price, status))
        changed = cur.rowcount
        
print(changed)
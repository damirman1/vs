# 07 Поиск одной доставки 
# 1. Создайте task_07.py. Запросите у пользователя целый ID через input и int. 
# 2. Найдите запись с этим ID. Значение передайте параметром отдельно от SQL. 
# 3. Покажите один словарь или сообщение Запись не найдена. Проверьте ID 3 и ID 777. 

from db import connect_db

delivery_id = int(input("Delivery ID: "))

sql = """
SELECT id, cargo, price, status
FROM lesson_deliveries
WHERE id = %s;
"""

with connect_db() as conn:
    with conn.cursor() as cur:
        cur.execute(sql, (delivery_id,))
        row = cur.fetchone()
        
    if row is None:
        print("Запись не найдена.")
    else:
        print(row)
# 04 Что ещё ждёт отправки 
# 1. Создайте task_04.py. Покажите только доставки со статусом ready. 
# 2. Верните id, cargo, price и status, отсортируйте по id. 
# 3. Проверьте, что завершённые доставки не попали в ответ. Исходные статусы не меняйте. 

from db import connect_db

sql = """
SELECT id, cargo, price, status
FROM lesson_deliveries
WHERE status = 'ready'
ORDER BY id;
"""
with connect_db() as conn:
    with conn.cursor() as cur:
        cur.execute(sql)
        rows = cur.fetchall()
        
    for row in rows:
        print(row)
# 09 Посылка доставлена 
# 1. Создайте task_09.py. Для тестовой доставки с ID 99 измените status с ready на done. 
# 2. Передайте новый статус и ID отдельно от текста SQL. 
# 3. Выведите число изменённых строк. Проверьте через SELECT, что остальные пять доставок не изменились. 

from db import connect_db

delivery_id = 99
new_status = "done"

sql = """
UPDATE lesson_deliveries
SET status = %s
WHERE id = %s
"""

with connect_db() as conn:
    with conn.cursor() as cur:
        cur.execute(sql, (new_status, delivery_id))
        changed = cur.rowcount
        
print(changed)
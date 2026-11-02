
from db import connect_db

# 02 Весь журнал доставок 
# 1. После подготовки таблицы создайте task_02.py. 
# 2. Получите id, cargo, price и status всех доставок из lesson_deliveries. 
# 3. Упорядочите записи по id и выведите каждую запись отдельной строкой. 

sql = """
SELECT id, cargo, price, status
FROM lesson_deliveries
ORDER BY id;
"""

with connect_db() as conn:
    with conn.cursor() as cur:
        cur.execute(sql)
        rows = cur.fetchall()
        
    for row in rows:
        print(row)
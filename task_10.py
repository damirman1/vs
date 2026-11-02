# 10 Удаление своей тестовой записи 
# 1. Создайте task_10.py. Сначала просмотрите доставку 99 через SELECT. 
# 2. Удалите только эту тестовую строку через параметризованный запрос по ID. 
# 3. Выведите число удалённых строк. Затем повторите поиск: запись не должна находиться, исходные пять строк должны остаться. 

from db import connect_db

delivery_id = 99

sql_select = """
SELECT id 
FROM lesson_deliveries 
WHERE id = %s
"""

sql_delete = """
DELETE 
FROM lesson_deliveries 
WHERE id = %s
"""

sql_count = """
SELECT COUNT(*) 
FROM lesson_deliveries
"""

with connect_db() as conn:
    with conn.cursor() as cur:
        cur.execute(sql_select, (delivery_id,))
        found = cur.fetchone()
        print(found)

        cur.execute(sql_delete, (delivery_id,))
        changed = cur.rowcount
        print(changed)

        cur.execute(sql_select, (delivery_id,))
        found_after_delete = cur.fetchone()
        print(found_after_delete)

        cur.execute(sql_count)
        total_rows = cur.fetchone()[0]
        print(total_rows)
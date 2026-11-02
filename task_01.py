from db import connect_db

# 01 Проверка уже знакомого подключения
# 1. Создайте файл task_01.py рядом с db.py и .env. 
# 2. Выполните запрос, который возвращает число 1 с именем столбца result. 
# 3. Выведите полученную строку. Таблицы и данные пока не меняйте. 

sql = """
SELECT 1 AS result;
"""
with connect_db() as conn:
    with conn.cursor() as cur:
        cur.execute(sql)
        row = cur.fetchone()

    if row is None:
        print("Запись не найдена!")
    else:
        print(row)
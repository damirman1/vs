from db import connect_db

# 01 Знакомое подключение 
# 1. Создайте папку terminal_shop и локальный .env с вашей строкой подключения. 
# 2. Добавьте db.py и выполните SELECT 1 AS result через check_connection.py. 
# 3. Получите словарь с result равным 1. Не печатайте строку подключения. 

with connect_db() as conn:
    with conn.cursor() as cur:
        cur.execute("SELECT 1 AS result;")
        row = cur.fetchone()
        
print(row)



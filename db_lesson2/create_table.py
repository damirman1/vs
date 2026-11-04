from db import connect_db

# 02 Полка с первыми товарами 
# 1. Создайте отдельную таблицу terminal_products по схеме из мануала. 
# 2. Заполните пустую таблицу пятью исходными товарами из 02_seed.sql один раз. 
# 3. Проверьте id, name, price и stock через SELECT. Остальные учебные таблицы не меняйте. 

sql = """
CREATE TABLE IF NOT EXISTS terminal_products (
    id SERIAL PRIMARY KEY(id > 0),
    name TEXT NOT NULL,
    price INTEGER NOT NULL CHECK(price > 0),
    stock INTEGER NOT NULL CHECK(stock >= 0)
);
"""

with connect_db() as conn:
    with conn.cursor() as cur:
        cur.execute(sql)
        
print("Таблица создана!")
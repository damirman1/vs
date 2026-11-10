from db import connect_db

# 10 Проверка готового магазина 
# 1. Добавьте изученные функции в app.py и меню по образцу мануала. 
# 2. Проверьте каталог, поиск, цену, покупку, добавление, пустой результат и неверный ввод. 
# 3. Закройте программу, откройте снова и убедитесь, что изменения сохранились. 
# 4. Добавьте README.md и загрузите код в уже созданный Git-репозиторий. .env и пароль не должны попасть в коммит. 

def show_catalog():
    sql = """
        SELECT id, name, price, stock
        FROM terminal_products
        ORDER BY id;
    """
    with connect_db() as conn:
        with conn.cursor() as cur:
            cur.execute(sql)
            rows = cur.fetchall()
    
    print("-----Каталог товаров-----")
    for row in rows:
        print(row["id"], row["name"], row["price"], row["stock"])
from step_04 import read_int
from db import connect_db

# 06 Новая цена на полке 
# 1. Запросите ID и новую положительную целую цену. 
# 2. Измените цену только выбранного товара. 
# 3. Покажите, сохранилась ли цена. Снова откройте каталог и проверьте результат. 

def change_price():
    product_id = read_int("ID товара: ", 1)
    new_price = read_int("Новая цена: ", 1)
    
    sql = """
        UPDATE terminal_products
        SET price = %s
        WHERE id = %s;
    """
    with connect_db() as conn:
            with conn.cursor() as cur:
                cur.execute(sql, (new_price, product_id))
                changed = cur.rowcount
    if changed == 1:
        print("Цена изменена!")
    else:
        print("Товар не найден!")
        
change_price()
from db import connect_db
from step_04 import read_int

# 07 Покупка одной штуки 
# 1. Запросите ID товара и уменьшите остаток ровно на одну штуку. 
# 2. Покупка должна проходить только при stock больше нуля. 
# 3. Не меняйте цену. Для отсутствующего или закончившегося товара выведите общее понятное сообщение. 

def buy_one():
    product_id = read_int("ID товара: ", 1)
    
    sql = """
        UPDATE terminal_products
        SET stock = stock - 1
        WHERE id = %s AND stock > 0;
    """
    with connect_db() as conn:
            with conn.cursor() as cur:
                cur.execute(sql, (product_id,))
                changed = cur.rowcount
    if changed == 1:
        print("Покупка совершена!")
    else:
        print("Товар не найден или закончился!")
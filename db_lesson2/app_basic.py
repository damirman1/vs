from step_03 import show_products
from step_04 import find_product
import psycopg

# 05 Первое готовое меню 
# 1. Соберите app_basic.py из готовых функций чтения. 
# 2. Добавьте повторяющееся меню: 1 каталог, 2 поиск по ID, 0 выход. 
# 3. Обработайте неизвестный пункт без завершения программы. Данные по-прежнему хранятся в Neon. 

def main():
    while True:
        print("=========Магазин ТЕХМЕЛОЧЕЙ=========")
        print("1. Каталог")
        print("2. Поиск по ID")
        print("0. Выход")
        choice = input("Выберите действие: 1, 2, 0")
        try:
            if choice == "1":
                show_products()
            elif choice == "2":
                find_product()
            elif choice == "0":
                break
            else:
                print("Такого пункта не существует!")
        except psycopg.Error:
            print("Запрос не выполнен! Проверьте подключение к базе данных")
            
if __name__ == "__main__":
    main()
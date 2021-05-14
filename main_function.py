# Подключаем библиотеку для работы с базой данных
import sqlite3

# Функция для запросов к БД. В аргумент поступает сам запрос.
def main_function(sql):
    try:
        # Обращаемся к БД, если её нет, то она автоматически создается
        connection = sqlite3.connect("test.db")

        # Чтобы выполнить запрос к таблице в базе данных, нам нужно использовать объект курсора
        cursor = connection.cursor()

        # Теперь можем выполнить запрос к БД
        cursor.execute(sql)
        result = cursor.fetchall()
        
        # Фиксируем изменения в БД
        connection.commit()
        
        # Не забываем закрыть соединение
        connection.close()
        return result
    except Exception as e:
        print(e)

print(main_function("SELECT * FROM table_name;"))

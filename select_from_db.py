# Подключаем библиотеку для работы с базой данных
import sqlite3

# Обращаемся к БД, если её нет, то она автоматически создается
connection = sqlite3.connect("test.db")

# Чтобы выполнить запрос к таблице в базе данных, нам нужно использовать объект курсора
cursor = connection.cursor()

# Теперь можем выполнить запрос к БД
cursor.execute("SELECT * FROM table_name;")
a = cursor.fetchall()
print(a)
# Фиксируем изменения в БД
connection.commit()
print(a)
# Не забываем закрыть соединение
connection.close()
print(a)

# Подключаем библиотеку для работы с базой данных
import sqlite3

# Обращаемся к БД, если её нет, то она автоматически создается
connection = sqlite3.connect("test.db")

# Чтобы создать таблицу в базе данных, нам нужно использовать объект курсора
cursor = connection.cursor()

# Теперь можем выполнить запрос к БД
cursor.execute("CREATE TABLE table_name (`id` INTEGER PRIMARY KEY AUTOINCREMENT, `column2` text, `column3` text);")

# Фиксируем изменения в БД
connection.commit()

# Не забываем закрыть соединение
connection.close()

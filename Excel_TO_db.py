import pandas as pd
import sqlite3

# Считываем данные из файла Excel
excel_data = pd.read_excel('21школа.xlsx')

# Создаем подключение к базе данных SQLite
conn = sqlite3.connect('DataBase.db')

# Используем метод to_sql библиотеки pandas для записи данных в базу данных SQLite
excel_data.to_sql('data', conn, if_exists='replace', index=False)

# Закрываем соединение
conn.close()
print("Готово")
import configparser
import mysql.connector
import connection_to_db as c
import functions as f


hostname = 'имя хоста'
username = 'имя пользователя'
user_password = 'пароль пользователя'

connection = c.create_connection_with_server(hostname, username, user_password)
connection = c.create_connection_with_bd(hostname, username, user_password)

try:
    c.execute_sql(c.create_table_log(), connection)
except:
    pass

array_logs = f.file_into_array()

for log in array_logs:
    c.execute_sql(f.seporator(log), connection)

# Создание объекта конфигурации и чтение файла config.ini
config = configparser.ConfigParser()
config.read('config.ini')

# Получение значений для подключения к базе данных
host = config.get('Database', 'host')
username = config.get('Database', 'username')
password = config.get('Database', 'password')
database = config.get('Database', 'database')

# Подключение к базе данных
connection = mysql.connector.connect(
    host=host,
    user=username,
    password=password,
    database=database
)

# Использование подключения к базе данных
cursor = connection.cursor()
cursor.execute("SELECT * FROM Log")
result = cursor.fetchall()
for row in result:
    print(row)

# Закрытие соединения с базой данных
cursor.close()
connection.close()




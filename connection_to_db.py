import functions as f
import mysql.connector
from mysql.connector import connect, Error


# Подключение к серверу и создание бд
def create_connection_with_server(host_name, user_name, user_password, query_to_create_db="CREATE DATABASE "придумайте название для базы данных""):
    try:
        with connect(
            host = host_name,
            user = user_name,
            password = user_password,
        ) as connection:

            new_db = connection.cursor()
            new_db.execute(query_to_create_db)
    except Error as e:
        f.prompt(e)



# Подключение к самой бд
def create_connection_with_bd(host_name, user_name, user_password, db_name='напишите название базы данных'):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password,
            database=db_name
        )
        f.prompt("Connection to MySQL DB successful")
    except Error as e:
        f.prompt(f"The error '{e}' occurred")
    return connection



# Функция для выполнения кода SQL
def execute_sql(query, connection):
    with connection.cursor() as cursor:
        cursor.execute(query)
        connection.commit()


# Создание таблицы 
def create_table_log():
    table_log =  '''
    create table Log
    (
    IP_Address varchar(20) not null check(IP_Address rlike('^([0-9]{1,3})\\.([0-9]{1,3})\\.([0-9]{1,3})\\.([0-9]{1,3})$')),
    Identity varchar(400) not null,
    Username varchar(400) not null,
    Date_Log varchar(20) not null,
    Time_Log time not null,
    Zone varchar(7) not null,
    Method varchar(30) not null,
    Requested_Resource varchar(100) not null,
    http_Version varchar(100) not null,
    Status_Code varchar(8) not null,
    Response_Size varchar(20) not null,
    Referer varchar(100) not null,
    User_Agent varchar(400) not null
    );
	'''
    return table_log


# Добавление данных
def insert_data(IP_Address, Identity, Username, date_log, time_log, zone,
 Method, requested_resource, http_version, status_code, response_size, referer, user_agent):
    insert = f'''
    insert into Log(IP_Address, Identity, Username, date_log, time_log, zone,
    Method, requested_resource, http_version, status_code, response_size, referer, user_agent)

    values('{IP_Address}', '{Identity}', '{Username}', '{date_log}', '{time_log}', '{zone}',
    '{Method}', '{requested_resource}', '{http_version}', '{status_code}', '{response_size}', '{referer}', '{user_agent}');
    '''
    return insert


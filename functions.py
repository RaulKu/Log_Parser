import re
import connection_to_db as c
import configparser

# Создание объекта конфигурации и чтение файла config.ini
config = configparser.ConfigParser()
config.read('config.ini')

# Получение значений из конфигурационного файла
log_directory = config.get('Settings', 'log_directory')
file_mask = config.get('Settings', 'file_mask')
max_size = config.getint('Settings', 'max_size')

def prompt(msg):
    print(msg)

def getter(msg):
    return input(msg)

def file_into_array(msg_get_file_way='Input path: ', msg_if_file_not_founded='File not founded')-> list:
    try:
        filename = 'укажите путь к файлу с логами'
        with open(filename, 'r+') as f:
            array_logs = f.readlines()
        with open(filename, 'w+') as f:
            f.seek(0)

        return array_logs
    except FileNotFoundError:
        raise Exception(msg_if_file_not_founded)


def seporator(log_line):
    log_pattern = r'.+ (\d{1,3}\.\d{1,3}\.\d{0,3}\.\d{1,3}) (\S+) (\S+) \[(\d{2}\/\w{3}\/\d{4}) (\d{2}:\d{2}:\d{2})\] "(\S+)\s?(\S+)?\s?(\S+)?" (\d{3}) (\d+|-)\s?"?([^"]*)"?\s?"?([^"]*)?"?'

    match = re.match(log_pattern, log_line)
    if match:
        IP_Address = match.group(1)
        Identity = match.group(2)
        Username = match.group(3)
        Date_Log = match.group(4)
        Time_Log = match.group(5)
        Zone = '-'
        Method = match.group(6)
        Requested_Resource = match.group(7)
        HTTP_Version = match.group(8)
        Status_Code = match.group(9)
        Response_Size = match.group(10)
        Referer = match.group(11)
        User_Agent = match.group(12)

        return c.insert_data(IP_Address, Identity, Username, Date_Log, Time_Log, Zone, Method, Requested_Resource, HTTP_Version, Status_Code, Response_Size, Referer, User_Agent)

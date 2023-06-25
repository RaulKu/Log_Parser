import PySimpleGUI as sg
import mysql.connector
from crontab import CronTab
from dateutil.parser import parse

# Функция для подключения к базе данных
def connect_to_database(host, username, password):
    try:
        # Устанавливаем соединение с базой данных
        conn = mysql.connector.connect(
            host=host,
            user=username,
            password=password,
            database='db_for_parser'  # Замените на имя вашей базы данных
        )
        return conn
    except mysql.connector.Error as error:
        print('Ошибка подключения к базе данных:', error)

# Функция для получения данных из таблицы "Log"
def get_logs(connection, filter_ip=None, filter_date=None):
    try:
        cursor = connection.cursor()
        query = "SELECT * FROM Log"
        conditions = []
        if filter_ip:
            conditions.append(f"IP_Address = '{filter_ip}'")
        if filter_date:
            conditions.append(f"Date_Log = '{filter_date}'")
        if conditions:
            query += " WHERE " + " AND ".join(conditions)
        cursor.execute(query)
        logs = cursor.fetchall()
        return logs
    except mysql.connector.Error as error:
        print('Ошибка при получении данных из базы данных:', error)

# Функция для добавления задачи планировщика Cron
def add_cron_job(date, time):
    # Создание планировщика Cron
    cron = CronTab(user=True)

    # Удаление всех предыдущих задач планировщика
    cron.remove_all()

    # Разделение времени на значения минут и часов
    hour, minute = time.split(':')

    # Разделение даты на год, месяц и день
    year, month, day = date.split('-')

    # Добавление новой задачи для выполнения кода в выбранную дату и время
    job = cron.new(command = "укажите свой интерпритарор python и путь к файлу main.py")  # Замените на путь к вашему файлу
    job.setall(f"{minute} {hour} {day} {month} *")

    # Запись изменений в планировщик Cron
    cron.write()



# Определение макета формы
layout = [
    [sg.Text('Название хоста'), sg.InputText(size=30)],
    [sg.Text('Имя пользователя'), sg.InputText(size=20)],
    [sg.Text('Пароль от MySQL'), sg.InputText(size=20)],
    [sg.Text('Фильтрация по IP'), sg.InputText(size=(20), key='-FILTER-')],
    [sg.Text('Фильтрация по дате'), sg.InputText(size=(20), key='-DATE-')],
    [sg.Button(button_text='Подключиться к базе'), sg.Button('Вывести данные'), sg.Button('Добавить задачу Cron')],
    [sg.Text('Данные из базы данных:')],
    [sg.Listbox(values=[], size=(250, 70), key='-LISTBOX-')],
    [sg.Cancel()]
]

# Создание окна
window = sg.Window('File Compare', layout)
connection = None  # Инициализация переменной для хранения соединения с базой данных
logs = []  # Инициализация переменной для хранения данных из базы данных

while True:
    event, values = window.read()

    if event in (None, 'Exit', 'Cancel'):
        break
    elif event == 'Подключиться к базе':
        host = values[0]
        username = values[1]
        password = values[2]

        # Подключение к базе данных
        connection = connect_to_database(host, username, password)

        if connection:
            print('Успешное подключение к базе данных')
            sg.popup('Успешное подключение')
        else:
            sg.popup('База не подключена, проверьте введенные данные')

    elif event == 'Вывести данные':
        filter_ip = values['-FILTER-'] if values['-FILTER-'] else None
        filter_date = values['-DATE-'] if values['-DATE-'] else None

        if connection:
            # Получение данных из базы данных с возможными фильтрами по IP и дате
            logs = get_logs(connection, filter_ip, filter_date)
            if logs:
                # Очистка списка перед добавлением новых данных
                window['-LISTBOX-'].update(values=logs)

    elif event == 'Добавить задачу Cron':
        date_str = sg.popup_get_text('Введите дату (YYYY-MM-DD)')
        time_str = sg.popup_get_text('Введите время (HH:MM)')
        try:
            date = parse(date_str).strftime('%Y-%m-%d')
            time = parse(time_str).strftime('%H:%M')
            add_cron_job(date, time)
            sg.popup('Задача Cron успешно добавлена')
        except ValueError:
            sg.popup('Ошибка при вводе даты или времени')

window.close()

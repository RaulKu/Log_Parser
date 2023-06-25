from flask import Flask, render_template, request
import jsonify
import datetime
import json
import logging
import re 
from datetime import datetime
from parser import log_error_to_file



app = Flask(__name__)
app.template_folder = './templates'

# Фейковая база данных пользователей
users = []

#запись логов и ошибок в файл
@app.route('/', methods=['GET'])
def index():
    log_error_to_file()
    return render_template('index.html')

#регистрация и авторизация
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        # Проверка введенных данных
        if username and password:
            # Проверка пользователя в базе данных
            if any(user['username'] == username and user['password'] == password for user in users):
                return render_template('home.html')
            else:
                return 'Неверное имя пользователя или пароль'
        else:
            return 'Введите имя пользователя и пароль'
    
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        # Проверка введенных данных
        if username and password:
            # Проверка уникальности имени пользователя
            if any(user['username'] == username for user in users):
                return 'Имя пользователя уже занято'
            else:
                # Добавление нового пользователя в базу данных
                users.append({'username': username, 'password': password})
                return render_template('login.html')
        else:
            return 'Введите имя пользователя и пароль'
    
    return render_template('register.html')


#запуск
if __name__ == '__main__':
    app.run()






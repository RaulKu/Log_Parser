
## Инструкции по запуску

### Шаг 1: Установка зависимостей


### 1 Клонируйте репозиторий:

git clone https://github.com/RaulKu/Log_Parser

### 2 Перейдите в каталог проекта: 

cd apache-log-parser

### 3 Создайте виртуальное окружение (опционально, но рекомендуется): 

python -m venv venv

### 4 Активируйте виртуальное окружение:

 ◦ В Windows: venv\Scripts\activate
 ◦ В macOS и Linux: source venv/bin/activate

### Для успешного запуска этих файлов, следуйте указанным ниже шагам.
### Перед запуском приложения вам потребуется установить необходимые зависимости. Выполните следующую команду для установки зависимостей:

### 5 Установите необходимые зависимости: 

pip install -r requirements.txt




### Шаг 2: Подготовка базы данных и файла config.ini

Перед запуском приложения вам необходимо подготовить базу данных MySQL и файл config.ini. Следуйте инструкциям ниже:

1. Запустите MySQL-сервер.
2. Откройте файл `connection_to_db.py` и внесите следующие изменения:
   - Замените `'напишите название базы данных'` на желаемое название базы данных.
   - Замените `'CREATE DATABASE "придумайте название для базы данных"'` на команду для создания базы данных. Например: `'CREATE DATABASE mydatabase'`.
3. Сохраните файл `connection_to_db.py`.
4. Измените данные в файле config.ini на свои и сохраните изменения.

### Шаг 3: Запуск приложения

Теперь, когда зависимости установлены и база данных подготовлена, вы можете запустить приложение. Выполните следующую команду для запуска:

```
python app.py

```

После успешного запуска приложение будет доступно по адресу [http://localhost:5000/](http://localhost:5000/).

### Шаг 4: Использование приложения

Откройте веб-браузер и перейдите по адресу [http://localhost:5000/](http://localhost:5000/) для использования приложения. Вы сможете зарегистрироваться, войти в систему.
Это нужно для того, что бы сформировать log файлы.

### Шаг 5: Использование main.py

Теперь, когда log файл заполнен, вы можете запустить main.py для сохранения log файлов в базу. Выполните следующую команду для запуска:

```
python main.py

```

### Шаг 6: Использование forms.py

Теперь, когда log файл заполнен и база данных подготовлена, вы можете запустить форму. Выполните следующую команду для запуска:

```
python forms.py

```

### Приложение также содержит возможность добавления задачи планировщика Cron для выполнения кода в определенное время и дату. Для использования этой функциональности запустите файл `forms.py` и следуйте инструкциям в приложении.

---

Следуя этим инструкциям, вы сможете успешно запустить и использовать приложение. Убедитесь, что у вас установлены все необходимые зависимости и база данных подготовлена перед запуском!.

### Если вы хотите воспользоваться приложением повторно, то вам нужно зайти на сайт и сделать любые действия, для формирования новых логов, затем повторно запустить файл main.py, для сохранения новых log файлов к имеющимся файлам в базе данных.

import logging

def log_error_to_file():
    logging.basicConfig(
        filename= your_log_file,  # имя файла для записи логов
        format='%(asctime)s %(levelname)s %(message)s',
        level=logging.DEBUG
    )
    try:
        result = 1 / 0
    except Exception as e:
        # записываем лог ошибки
        logging.error('Ошибка: %s', e)

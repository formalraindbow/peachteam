import json
import gspread
from oauth2client.service_account import ServiceAccountCredentials


# Функция для нормализации текста (замена ё на е)
def normalize_text(text):
    return text.replace('ё', 'е').replace('Ё', 'Е') if text else ''


# Функция для чтения JSON файла
def load_json(json_file):
    with open(json_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return data


# Настройка доступа к Google Sheets
def connect_to_google_sheets(creds_file, sheet_name):
    scope = ['https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/drive']
    creds = ServiceAccountCredentials.from_json_keyfile_name(creds_file, scope)
    client = gspread.authorize(creds)
    sheet = client.open(sheet_name).sheet1
    return sheet


# Функция для получения ФИО из Google Sheets
def get_fio_from_google_sheets(sheet):
    # Читаем все данные с листа
    data = sheet.get_all_records()
    # Предположим, что ФИО в первых трех столбцах
    fio_google = []
    for row in data:
        fio = (
            normalize_text(row.get('Фамилия', '')),
            normalize_text(row.get('Имя', '')),
            normalize_text(row.get('Отчество', ''))
        )
        fio_google.append(fio)
    return fio_google


# Функция для получения ФИО и номеров пользователей из JSON
def get_fio_from_json(data):
    fio_json = {}
    for user_id, values in data.items():
        if len(values) >= 4:  # Проверяем, что есть хотя бы 4 элемента
            fio = tuple(normalize_text(value) for value in values[1:4])
            fio_json[user_id] = fio
    return fio_json


# Функция для сравнения списков ФИО
def compare_fio(fio_json, fio_google):
    matched = []
    unmatched = []
    unmatched_ids = []

    for user_id, fio in fio_json.items():
        if fio in fio_google:
            matched.append(fio)
        else:
            unmatched.append(fio)
            unmatched_ids.append(user_id)

    return matched, unmatched, unmatched_ids


# Основная функция
def main(json_file, creds_file, sheet_name):
    # Шаг 1: Загрузить данные из JSON
    json_data = load_json(json_file)

    # Шаг 2: Подключиться к Google Sheets и загрузить данные
    sheet = connect_to_google_sheets(creds_file, sheet_name)
    fio_google = get_fio_from_google_sheets(sheet)

    # Шаг 3: Получить ФИО из JSON
    fio_json = get_fio_from_json(json_data)

    # Шаг 4: Сравнить ФИО
    matched, unmatched, unmatched_ids = compare_fio(fio_json, fio_google)

    # Подсчет количества
    num_matched = len(matched)
    num_unmatched = len(unmatched)

    # Шаг 5: Вывести результат
    print(f"Количество совпавших записей: {num_matched}")
    print(f"Количество несовпавших записей: {num_unmatched}")
    print(f"айди пользователей с несовпавшими записями: {unmatched_ids}")

    # Вывести сами списки
    print(f"Совпавшие записи: {matched}")
    print(f"Несовпавшие записи: {unmatched}")


# Вызов основной функции
if __name__ == "__main__":
    json_file = '/Users/asya/Desktop/бот/guests_posvat.json'  # Путь к вашему JSON файлу
    creds_file = '/Users/asya/Downloads/posvat-435711-9183a38db040.json'  # Путь к файлу с учетными данными Google API
    sheet_name = 'посвят'  # Имя вашей Google Таблицы
    main(json_file, creds_file, sheet_name)

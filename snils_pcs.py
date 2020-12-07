import os
import json

# Итерируемся по папкам

# Получаем текущий рабочий каталог
import xlsxwriter

current_dir = os.getcwd()

# Получаем список папок в директории data
lst_folders = os.listdir(f'{current_dir}/data')
work_dir = f'{current_dir}'+'/data'

# Берем название папки, прописываем путь внутрь этой папки

def parse_json(path):
    path = f'data/{path}/{path}.json'
    with open(path,'r',encoding='utf-8') as f:
        data= json.load(f)
    return data



def parse_snils(data):
        FIO = f'{data["lastname"]} {data["firstname"]} {data["middlename"]}'
        return FIO,data['snils']



dic_snils = {}
count_rows = 0
name_file = 'fio_snils.xlsx'
# Создаем объект
workbook = xlsxwriter.Workbook(name_file)
# Устанавливаем название листа
worksheet = workbook.add_worksheet('Лист 1')
# Указываем стиль для заголовков
bold = workbook.add_format({'bold': True})
# Создаем заголовки
worksheet.write('A1', 'ФИО', bold)
worksheet.write('B1', 'СНИЛС', bold)
for name_folder in lst_folders:

    # Открываем json используя название папки
    data = parse_json(name_folder)
    # Получаем фио и снилс
    fio_snils = parse_snils (data)
    worksheet.write_row(count_rows, 0, list(fio_snils))
    count_rows += 1
workbook.close()
"""
Извлекаем данные

:Для начала реализуем функциональность создания папки с именем пользователя ,куда будем копировать содержимое базовой папки
В последующем реализуем  функции парсинга файла и создания таблицы эксель
"""

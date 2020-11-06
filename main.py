import os
import json

# Итерируемся по папкам

# Получаем текущий рабочий каталог
current_dir = os.getcwd()

# Получаем список папок в директории data
lst_folders = os.listdir(f'{current_dir}/data')
work_dir = f'{current_dir}'+'/data'

# Берем название папки, прописываем путь внутрь этой папки
def open_json(path):
    """
    Функция для парсинга json
    path = путь к файлу
    :return: строку
    """
    path = f'data/{path}/{path}.json'

    with open(path,'r',encoding='utf-8') as f:
        bar= json.load(f)
        name_folder = f'{bar["lastname"]}_{bar["firstname"]}_{bar["middlename"]} '
    return name_folder

for name_folder in lst_folders:
    # Открываем json используя название папки
    fio = open_json(name_folder)
    # Создаем папку с таким же именем

    os.renames(f'data/{name_folder}',f'data/{fio}')

"""
Извлекаем данные

:Для начала реализуем функциональность создания папки с именем пользователя ,куда будем копировать содержимое базовой папки
В последующем реализуем  функции парсинга файла и создания таблицы эксель
"""

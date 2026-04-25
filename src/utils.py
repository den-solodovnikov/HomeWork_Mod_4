import json
import os
from typing import Any

from src.category import Category
from src.product import Product


def read_json(path) -> Any | None:
    """ Функция считывания данных из JSON-файла. """
    try:
        full_path = os.path.abspath(path)
        with open(full_path, 'r', encoding="utf-8") as json_file:
            print(f'read_json: {full_path}')
            data = json.load(json_file)
        return data
    except FileNotFoundError:
        print("Ошибка. Файл не найден")



def create_objects_from_json(data: dict) -> list:
    """ Функция наполнения объектов Product и Category из внешних данных. """
    categories = []
    for category in data:
        products = []
        for product in category['products']:
            products.append(Product(**product))
        category['products'] = products
        categories.append(Category(**category))
    return categories


if __name__ == '__main__':
    data_products = read_json('../data/products.json')
    print(data_products)
    categories = create_objects_from_json(data_products)
    print(categories[0].name)

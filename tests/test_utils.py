import unittest
from unittest.mock import patch

import pytest

from src.category import Category
from src.product import Product
from src.utils import read_json, create_objects_from_json


@patch('json.load')
@patch('builtins.open', new_callable=unittest.mock.mock_open)
def test_read_json_success(mock_open, mock_load):
    mock_load.return_value = {'name': 'Iphone', 'price': 10000}
    assert read_json('../data/products.json') == {'name': 'Iphone', 'price': 10000}
    mock_open.assert_called_once_with('D:\\PYTHON\\data\\products.json', 'r', encoding="utf-8")


def test_read_json_error():
    # Тестируем поведение при ошибке (например, файл не найден)
    with pytest.raises(FileNotFoundError) as excinfo:
        open("bad_path.json")

    assert "bad_path.json" in str(excinfo.value)


test_data = [
    (
        # Входные данные
        [
            {
                "name": "Электроника",
                "description": "Электротовары",
                "products": [
                    {"name": "Смартфон", "description": "Красный", "price": 50000, "quantity": 5},
                ]
            }
        ],
        # Ожидаемый результат
        [
            Category(
                name="Электроника",
                description="Электротовары",
                products=[
                    Product(name="Смартфон", description="Красный", price=50000, quantity=5)
                ]
            )
        ]
    ),
    (
        # Пустой список категорий
        [],
        []
    ),
    (
        # Категория без товаров
        [
            {"name": "Книги", "description": "Канцелярия", "products": []}
        ],
        [
            Category(name="Книги", description="Канцелярия", products=[])
        ]
    )
]


@pytest.mark.parametrize("input_data, expected_result", test_data)
def test_create_objects_from_json(input_data, expected_result):
    result = create_objects_from_json(input_data)

    # Проверяем длину списка
    assert len(result) == len(expected_result)

    # Проверяем каждый объект по порядку
    for actual_category, expected_category in zip(result, expected_result):
        # Сравниваем поля категории
        assert actual_category.name == expected_category.name
        assert actual_category.description == expected_category.description

        # Сравниваем список товаров
        assert len(actual_category.products) == len(expected_category.products)

        for actual_product, expected_product in zip(actual_category._Category__products, expected_category._Category__products):
            assert actual_product.quantity == expected_product.quantity
            assert actual_product.name == expected_product.name
            assert actual_product.price == expected_product.price

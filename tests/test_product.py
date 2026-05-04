import pytest

from src.product import Product


def test_product_init(product):
    assert product.name == 'Iphone 15'
    assert product.description == '512GB, Gray space'
    assert product.price == 210000.0
    assert product.quantity == 8


@pytest.fixture
def new_product_dict():
    return {"name": "Iphone 15",
            "description": "512GB, Gray space",
            "price": 210000.0,
            "quantity": 8
            }

def test_new_product(product, new_product_dict):
    product.new_product(new_product_dict)
    assert product.name == 'Iphone 15'
    assert product.description == '512GB, Gray space'
    assert product.price == 210000.0
    assert product.quantity == 8


def test_prise_setter():
    product = Product("Iphone 15", "512GB, Gray space", 10000.0, 2)
    product.price = 20000.0
    assert product.price == 20000.0

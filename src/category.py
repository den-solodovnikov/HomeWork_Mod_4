from src.exceptions import ZeroQuantity
from src.product import Product


class Category:
    """ Класс представления категорий продуктов. """
    name: str
    description: str
    __products: list
    category_count = 0
    product_count = 0

    def __init__(self, name, description, products=None):
        self.name = name
        self.description = description
        self.__products = products if products else []
        Category.category_count += 1
        Category.product_count += len(products) if products else 0

    def add_product(self, new_product) -> str | None:
        """ Функция добавляет новый продукт в класс Category.
        Если такой товар уже присутствует, добавляет количество товаров.
        Ничего кроме смартфонов, травы газонной или других продуктов
        в список добавить нельзя. """
        if isinstance(new_product, Product) or issubclass(type(new_product), Product):
            for item in self.__products:
                try:
                    if item.quantity == 0:
                        raise ZeroQuantity('Нельзя добавить товар с нулевым количеством')
                except ZeroQuantity as ex:
                    print(str(ex))
                else:
                    if new_product.name == item.name:
                        item.quantity += new_product.quantity
                        item.price = new_product.price
                    else:
                        self.__products.append(new_product)
                    Category.product_count += 1
                    print('Товар добавлен успешно')
                finally:
                    print('Проверка на количество товаров прошла успешно')
        else:
            print(f'Нельзя добавить {new_product}, т.к. он не является объектом класса Product,\n'
                  f'а также его подклассов')
            raise TypeError

    def middle_price(self) -> float | None:
        try:
            return round(sum([product.price for product in self.__products]) / len(self.__products), 2)
        except ZeroDivisionError:
            return 0

    @property
    def products(self) -> str:
        """ Функция-геттер выводит строки, состоящие из списка продуктов с ценой и остатками. """
        products_list = list(
            f'{product.name}, {product.price} руб. Остаток: {product.quantity} шт.\n'
            for product in self.__products
        )
        return ''.join(products_list)

    def __str__(self):
        products_count = 0
        for item in self.__products:
            products_count += item.quantity
        products = f'{self.name}, количество продуктов: {products_count} шт.'

        return products

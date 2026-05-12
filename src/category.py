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

    def add_product(self, new_product) -> None:
        """ Функция добавляет новй продукт в класс Category.
         Если такой товар уже присутствует, добавляет количество товаров. """
        for item in self.__products:
            if new_product.name == item.name:
                item.quantity += new_product.quantity
                item.price = new_product.price
            else:
                self.__products.append(new_product)
        Category.product_count += 1

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

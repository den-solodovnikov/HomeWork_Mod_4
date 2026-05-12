class Product:
    """ Класс представления продуктов. """
    name: str
    description: str
    __price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    @classmethod
    def new_product(cls, new_product_dict: dict) -> Product:
        """ Функция создания нового продукта класса Product. """
        product = cls(
            name=new_product_dict.get("name"),
            description=new_product_dict.get("description"),
            price=new_product_dict.get("price"),
            quantity=new_product_dict.get("quantity")
        )

        return product

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, new_price: float) -> None:
        """ Функция-сеттер для установки новой цены товара с проверкой
         (отрицательная цена, цена ниже текущей). """
        if new_price <= 0:
            print('Цена не должна быть нулевая или отрицательная')
        elif self.__price <= new_price:
            self.__price = new_price
        else:
            print("""Новая цена продукта меньше текущей. Если вы согласны с понижением цены,
                                введите английскую "y", иначе, введите любой другой символ или нажмите Enter.\n"""
                  )
            user_accept = input().lower()
            if user_accept == "y":
                self.__price = new_price
                print(f"Установлена цена продукта: {self.__price} руб.")

    def __str__(self):

        return f'{self.name}, {self.price} руб. Остаток: {self.quantity} шт.'

    def __add__(self, other):

        return self.price * self.quantity + other.price * other.quantity

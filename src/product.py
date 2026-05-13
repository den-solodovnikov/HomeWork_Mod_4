from abc import ABC, abstractmethod


class BaseProduct(ABC):
    """ Абстрактный класс - родительский для класса Product"""
    @abstractmethod
    def price(self):
        pass


class MixinRepr:
    """ Класс-миксин, который при создании объекта, то есть при работе метода __init__,
    печататает в консоль информацию о том, от какого класса и с какими параметрами был создан объект. """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __repr__(self):
        dict_list = tuple(self.__dict__.values())
        return f'{self.__class__.__name__}{dict_list}'


class Product(MixinRepr, BaseProduct):
    """ Класс представления продуктов. """
    def __init__(self, name, description, price, quantity):
        super().__init__()
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

    # def __str__(self):
    #
    #     return f'{self.name}, {self.price} руб. Остаток: {self.quantity} шт.'

    def __add__(self, other):
        """ Функция сложения товаров только из одинаковых классов продуктов. """
        if type(other) is type(self):
            return self.price * self.quantity + other.price * other.quantity
        else:
            print('Нельзя складывать товары разных категорий')
            raise TypeError


class Smartphone(Product):
    """ Класс 'Смартфон' является наследником класса 'Product'. """
    efficiency: float
    model: str
    memory: int
    color: str

    def __init__(self, name, description, price, quantity, efficiency, model, memory, color):
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color

    @classmethod
    def new_product(cls, new_smartphone_dict: dict) -> Smartphone:
        """ Функция создания нового продукта класса Smartphone. """
        smartphone = cls(
            name=new_smartphone_dict.get("name"),
            description=new_smartphone_dict.get("description"),
            price=new_smartphone_dict.get("price"),
            quantity=new_smartphone_dict.get("quantity"),
            efficiency=new_smartphone_dict.get("efficiency"),
            model=new_smartphone_dict.get("model"),
            memory=new_smartphone_dict.get("memory"),
            color=new_smartphone_dict.get("color")
        )

        return smartphone


class LawnGrass(Product):
    """ Класс 'Трава газонная' является наследником класса 'Product'. """
    country: str
    germination_period: str
    color: str

    def __init__(self, name, description, price, quantity, country, germination_period, color):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color

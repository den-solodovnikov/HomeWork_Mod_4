class CategoryIterator:
    """ Класс принимает на вход объект класса Category и производит итерацию по товарам,
    которые хранятся в данной категории. Выполнение следующего шага итерации возвращает очередной товар категории. """
    def __init__(self, category_obj):
        self.category = category_obj
        self.index = 0

    def __iter__(self):
        """ Возвращает итератор. """
        self.index = 0
        return self

    def __next__(self):
        category_products = self.category.products.split('\n')
        if self.index < len(category_products):
            product = category_products[self.index]
            self.index += 1
            return product
        else:
            raise StopIteration

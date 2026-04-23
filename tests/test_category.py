def test_category_init(category_smartphone, category_tv):
    assert category_smartphone.name == 'Смартфоны'
    assert category_smartphone.description == (
        'Смартфоны, как средство не только коммуникации, '
        'но и получение дополнительных функций для удобства жизни'
    )
    assert len(category_smartphone.products) == 2
    assert category_smartphone.category_count == 4
    assert category_tv.product_count == 4

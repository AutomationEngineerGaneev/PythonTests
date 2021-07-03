from app.lib import create_apartment, add_apartment, search_apartments


def test_create_apartment():
    data = {
        'title': '2-х комнатная квартира',
        'number_of_rooms': 2,
        'area': 47,
        'region': 'Вахитовский район',
        'street': 'Вишневского',
        'house': '51',
        'apartment_number': '44',
        'price': 4_300_000
    }

    result = create_apartment(
        data['title'],
        data['number_of_rooms'],
        data['area'],
        data['region'],
        data['street'],
        data['house'],
        data['apartment_number'],
        data['price']
    )

    assert result == data

# тест добавить одну квартиру в пустой контейнер
def test_add_one_apartment_to_empty_container():
    container = []

    apartment = create_apartment(
        '2-х комнатная квартира',
        2,
        47,
        'Вахитовский район',
        'Вишневского',
        '51',
        '44',
        4_300_000
    )

    add_apartment(container, apartment)

    assert len(container) == 1
    assert apartment in container


# тестовый поиск квартир без параметров поиска
def test_search_apartments_without_search_parameters():
    container = []
    apartment1 = create_apartment(
        '2-х комнатная квартира',
        2,
        47,
        'Вахитовский район',
        'Вишневского',
        '51',
        '44',
        4_300_000
    )

    apartment2 = create_apartment(
        '1 комнатная квартира',
        1,
        27,
        'Авиастроительный район',
        'Лукина',
        '1',
        '25',
        2_000_000
    )

    apartment3 = create_apartment(
        '1 комнатная квартира',
        1,
        35,
        'Приволжский район',
        'Профессора Камая',
        '8',
        '45',
        3_200_000
    )

    add_apartment(container, apartment1)
    add_apartment(container, apartment2)
    add_apartment(container, apartment3)

    expected = [apartment1, apartment2, apartment3]

    result = search_apartments(container)

    assert result == expected

# def test_simple():
#     mylist = [1, 2, 3, 4, 5]
#     assert 3 in mylist
#
#
# def test_simple1():
#     mylist = [1, 2, 3, 4, 5]
#     assert 10 in mylist

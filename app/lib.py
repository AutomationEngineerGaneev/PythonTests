# функция с параметрами
def create_apartment(title, number_of_rooms, area, region, street, house, apartment_number, price):
    # словарь или Json
    return {
        'title': title,
        'number_of_rooms': number_of_rooms,
        'area': area,
        'region': region,
        'street': street,
        'house': house,
        'apartment_number': apartment_number,
        'price': price
    }


def add_apartment(container, apartment):
    # append Добавляет указанный элемент в конец списка.
    container.append(apartment)


# поиск квартир по па параметрам региона и цены
def search_apartments(container, search_regions=None, search_price=None):
    # результат поиска сравниваем с содержимым контейнера
    result = container

    if search_regions is not None:
        # Map применяет функцию к каждому элементу последовательности
        # и возвращает итератор с результатами.
        # Метод strip() возвращает копию строки
        search_regions = map(str.strip, search_regions)
        search_regions = list(map(str.lower, search_regions))

        def filter_by_regions(apartment):
            apartment_region = apartment['region']
            apartment_region = apartment_region.strip().lower()
            return apartment_region in search_regions

        result = list(filter(filter_by_regions, result))

    if search_price is not None:
        result = list(filter(lambda apartment: apartment['price'] < search_price, result))

    return result

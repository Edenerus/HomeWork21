from entity.shop import Shop
from entity.store import Storage
from entity.request import Request
from entity.courier import Courier
from entity.exceptions import BaseError


shop = Shop(
    items={
        'печеньки': 1,
        'собачки': 2,
        'коробки': 1,
        'мороженое': 2,
        'шоколад': 3,
    }
)

store = Storage(
    items={
        'печеньки': 10,
        'собачки': 20,
        'коробки': 15,
        'мороженое': 10,
        'шоколад': 10,
        'хлеб': 15,
    }
)

storages = {
    'магазин': shop,
    'склад': store,
}

def main():
    while True:

        for storage in storages:

            print(f"В {storage} хранится: {storages[storage].get_items()}")

        user_input = input(
            "Введите запрос в формате 'Доставить 3 собачки из склад в магазин'\n"
            "Введите 'stop' или 'стоп' чтобы продолжить\n"
        )

        if user_input in ["stop", 'стоп']:
            break

        try:
            request = Request(request=user_input, storages=storages)

        except BaseError as e:
            print(e.message)
            continue

        courier = Courier(request=request, storages=storages)

        try:
            courier.move()

        except BaseError as e:
            print(e.message)
            courier.cancel()


if __name__ == '__main__':
    main()

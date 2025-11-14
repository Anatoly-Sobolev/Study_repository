import collections

routes_data = {}
tickets_data = []


def add_route(number: int, capacity: int, route_description: str) -> bool:
    if number in routes_data:
        print(f"Ошибка: Маршрут с номером {number} уже существует.")
        return False
    if not isinstance(capacity, int) or capacity <= 0:
        print(f"Ошибка: Вместимость должна быть положительным целым числом.")
        return False

    routes_data[number] = {'capacity': capacity, 'route_description': route_description}
    print(f"✅ Маршрут №{number} добавлен: '{route_description}', вместимость: {capacity}.")
    return True


def add_ticket(route_number: int, date: str, departure_point: str, destination_point: str, price: float) -> bool:
    if route_number not in routes_data:
        print(f"Ошибка: Рейс с номером {route_number} не найден. Билет не может быть добавлен.")
        return False
    if not isinstance(price, (int, float)) or price <= 0:
        print(f"Ошибка: Цена должна быть положительным числом.")
        return False

    tickets_data.append({
        'route_number': route_number,
        'date': date,
        'departure_point': departure_point,
        'destination_point': destination_point,
        'price': price
    })
    print(
        f"✅ Билет на рейс №{route_number} ({departure_point} -> {destination_point}) от {date} добавлен. Цена: {price:.2f}.")
    return True


def find_trips_by_points(departure: str, destination: str):
    print(f"\n--- Поиск проездов из '{departure}' в '{destination}' ---")

    found_trips = []
    for ticket in tickets_data:
        if ticket['departure_point'] == departure and ticket['destination_point'] == destination:
            found_trips.append(ticket)

    if not found_trips:
        print(f"ℹ️ Проезды из '{departure}' в '{destination}' не найдены.")
    else:
        print(f"Найдено {len(found_trips)} проездов:")
        for trip in found_trips:
            route_desc = routes_data.get(trip['route_number'], {}).get('route_description', 'Неизвестный маршрут')
            print(
                f"  - Рейс №{trip['route_number']}, Дата: {trip['date']}, Цена: {trip['price']:.2f} (Маршрут: {route_desc})")

    return found_trips


def find_routes_by_occupancy(target_percentage: float, tolerance: float = 1.0):
    print(f"\n--- Поиск рейсов с заполняемостью около {target_percentage:.1f}% (+/- {tolerance:.1f}%) ---")

    route_runs_passenger_counts = collections.defaultdict(int)
    for ticket in tickets_data:
        key = (ticket['route_number'], ticket['date'])
        route_runs_passenger_counts[key] += 1

    found_routes_with_occupancy = []
    for (route_num, date), num_tickets in route_runs_passenger_counts.items():
        route_details = routes_data.get(route_num)

        if not route_details:
            continue

        capacity = route_details['capacity']
        if capacity == 0:  # Избегаем деления на ноль, если вместимость каким-то образом стала 0
            calculated_percentage = 0.0
        else:
            calculated_percentage = (num_tickets / capacity) * 100

        # Проверяем, находится ли рассчитанный процент заполняемости в пределах допустимого отклонения
        if abs(calculated_percentage - target_percentage) <= tolerance:
            found_routes_with_occupancy.append({
                'route_number': route_num,
                'date': date,
                'occupancy_percentage': calculated_percentage,
                'passengers': num_tickets,
                'capacity': capacity,
                'route_description': route_details['route_description']
            })

    if not found_routes_with_occupancy:
        print(f"ℹ️ Рейсы с заполняемостью около {target_percentage:.1f}% не найдены.")
    else:
        print(f"Найдено {len(found_routes_with_occupancy)} рейсов:")
        for item in found_routes_with_occupancy:
            print(f"  - Рейс №{item['route_number']} ({item['route_description']}), Дата: {item['date']}: "
                  f"Заполнено {item['passengers']}/{item['capacity']} мест ({item['occupancy_percentage']:.1f}%)")

    return found_routes_with_occupancy


def set_default_data():
    # 1. Добавление тестовых маршрутов
    print("\n--- Добавление маршрутов ---")
    add_route(101, 50, 'Москва - Тверь - Санкт-Петербург')
    add_route(102, 40, 'Санкт-Петербург - Новгород - Псков')
    add_route(103, 60, 'Москва - Тула - Орел')
    add_route(104, 30, 'Орел - Курск - Белгород')  # Для теста 100% заполняемости
    add_route(105, 100, 'Казань - Нижний Новгород')  # Для теста низкой заполняемости (1%)
    add_route(106, 20, 'Воронеж - Липецк')  # Для теста 75% заполняемости
    add_route(107, 40, 'Екатеринбург - Челябинск')  # Для теста 25% заполняемости



    print("\n--- Добавление проданных билетов ---")
    # Билеты для Рейса 101 (вместимость 50)
    add_ticket(101, '2023-10-26', 'Москва', 'Тверь', 800)
    add_ticket(101, '2023-10-26', 'Москва', 'Санкт-Петербург', 1500)
    add_ticket(101, '2023-10-26', 'Тверь', 'Санкт-Петербург', 900)
    add_ticket(101, '2023-10-26', 'Москва', 'Тверь', 800)
    add_ticket(101, '2023-10-26', 'Тверь', 'Санкт-Петербург', 900)
    # Итого для 101 на 2023-10-26: 5 билетов. Заполняемость: (5/50)*100 = 10%

    for _ in range(10):  # Еще 10 билетов на другой день
        add_ticket(101, '2023-10-27', 'Москва', 'Тверь', 800)
    # Итого для 101 на 2023-10-27: 10 билетов. Заполняемость: (10/50)*100 = 20%

    # Билеты для Рейса 102 (вместимость 40)
    for _ in range(20):  # 20 билетов
        add_ticket(102, '2023-10-26', 'Санкт-Петербург', 'Псков', 1200)
    # Итого для 102 на 2023-10-26: 20 билетов. Заполняемость: (20/40)*100 = 50%

    # Билеты для Рейса 103 (вместимость 60)
    for _ in range(30):  # 30 билетов
        add_ticket(103, '2023-10-26', 'Москва', 'Тула', 700)
    # Итого для 103 на 2023-10-26: 30 билетов. Заполняемость: (30/60)*100 = 50%

    # Билеты для Рейса 104 (вместимость 30) - 100% заполняемость
    for _ in range(30):  # 30 билетов
        add_ticket(104, '2023-10-28', 'Орел', 'Белгород', 600)
    # Итого для 104 на 2023-10-28: 30 билетов. Заполняемость: (30/30)*100 = 100%

    # Билеты для Рейса 105 (вместимость 100) - низкая заполняемость
    add_ticket(105, '2023-10-28', 'Казань', 'Нижний Новгород', 1800)
    # Итого для 105 на 2023-10-28: 1 билет. Заполняемость: (1/100)*100 = 1%

    # Билеты для Рейса 106 (вместимость 20) - 75% заполняемость
    for _ in range(15):  # 15 билетов
        add_ticket(106, '2023-10-29', 'Воронеж', 'Липецк', 450)
    # Итого для 106 на 2023-10-29: 15 билетов. Заполняемость: (15/20)*100 = 75%

    # Билеты для Рейса 107 (вместимость 40) - 25% заполняемость
    for _ in range(10):  # 10 билетов
        add_ticket(107, '2023-10-29', 'Екатеринбург', 'Челябинск', 1100)
    # Итого для 107 на 2023-10-29: 10 билетов. Заполняемость: (10/40)*100 = 25%

    # Попытка добавить билет на несуществующий рейс (должна вывести ошибку)
    add_ticket(999, '2023-10-30', 'ГородА', 'ГородБ', 500)

    # --- Выполнение поисковых задач ---

    # Задача 1: Перечень проездов от начального до конечного пункта назначения
    find_trips_by_points('Москва', 'Санкт-Петербург')
    find_trips_by_points('Санкт-Петербург', 'Псков')
    find_trips_by_points('Орел', 'Белгород')
    find_trips_by_points('Воронеж', 'Липецк')
    find_trips_by_points('НереальныйГород', 'ДругойГород')  # Пример, когда проезды не найдены

    # Задача 2: Перечень рейсов, выполненных с указанной заполняемостью
    # Используется параметр tolerance=1.0, что означает поиск рейсов с заполняемостью
    # в диапазоне [target_percentage - 1.0, target_percentage + 1.0].
    find_routes_by_occupancy(10.0)  # Ожидаем рейс 101 от 2023-10-26
    find_routes_by_occupancy(20.0)  # Ожидаем рейс 101 от 2023-10-27
    find_routes_by_occupancy(50.0)  # Ожидаем рейсы 102 и 103 от 2023-10-26
    find_routes_by_occupancy(100.0)  # Ожидаем рейс 104 от 2023-10-28
    find_routes_by_occupancy(1.0)  # Ожидаем рейс 105 от 2023-10-28
    find_routes_by_occupancy(75.0)  #
    [print() for i in range(10)]



def main():
    n = 10
    while n != 0:
        print("Систему учёта данных автовокзала\n")
        print("0 - Завершить программу")
        print("1 - Добавить проданный билет в базу данных")
        print("2 - Добавить новый маршрут в базу данных")
        print("3 - Найти маршруты по конечным населённым пунктам")
        print("4 - Найти марруты по заданныму проценту заполняемости")
        print()
        n = int(input("Введите номер команды: "))

        if n not in [0, 1, 2, 3, 4]: continue
        if n == 1:
            num = int(input("Введите номер маршрута: "))
            date = input("Введите дату формата YYYY-MM-DD: ")
            departure_point = input("Введите пункт отправления: ")
            destination_point = input("Ведите пункт прибытия: ")
            price = int(input("Введите стоимость билета: "))

            add_ticket(num, date, departure_point, destination_point, price)
            print()

        if n == 2:
            num = int(input("Введите номер маршрута: "))
            capacity = int(input("Введите вместимость : "))
            destination = input("Укажите насёлённые пункты. Формат: Москва - Тверь - Санкт-Петербург \n")
            add_route(num, capacity, destination)
            print()

        if n == 3:
            departure_point = input("Введите пункт отправления: ")
            destination_point = input("Ведите пункт прибытия: ")

            find_trips_by_points(departure_point, destination_point)
            print()

        if n == 4:
            occupancy = float(input("Введите процент заполняемости маршрута: "))
            find_routes_by_occupancy(occupancy)
            print()





if __name__ == "__main__":
    set_default_data()
    main()
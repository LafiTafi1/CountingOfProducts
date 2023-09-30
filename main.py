import sys

# 1. Приветствие. Список функций:
# 2. Посмотреть добавленные товары
# 3. Добавить товар
# 4. Удалить товар
# 5. Посчитать сумму товаров


# Хранение товаров
quantity_product = {}  # название и количество товара
price_product = {}  # название и цена за единицу товара


# Посмотреть список товаров
def view_all_products():

    if not price_product:
        print(f'\nПока вы не добавили ни одного товара. Чтобы сделать это, напишите цифру 2.\n')
        call_menu()
    else:
        for key, value in sorted(price_product.items()):
            print(f'\n{key.upper()} (стоимость: {value}, количество: {quantity_product[key]})\n')

        print('Что сделать дальше?\n1. Добавить ещё один товар\n 2. Выйти в главное меню\n')

        match input('Введите цифру: '):
            case '1':
                add_product()
            case '2':
                go_to_menu()
            case _:
                print('Упс, кажется ты не соблюдаешь правила :(\nК сожалению, я вынужден завершить программу')
                sys.exit()


# Добавить товар
def add_product():

    name_product = input('Введите название товара: ').upper()
    unit_price = float(input('Введите стоимость за единицу товара: '))
    quantity = int(input('Введите количество товара: '))

    quantity_product.update({name_product: quantity})
    price_product.update({name_product: unit_price})

    add_more()


def add_more():

    print(f'\nХотите добавить ещё один товар?\n 1. Да\n 2. Нет')

    match input('Введите цифру: ').upper():
        case '1':
            add_product()
        case '2':
            print(f'\nВы вышли в главное меню\n')
            go_to_menu()
        case _:
            print(f'Упс, кажется ты не соблюдаешь правила :(\n')
            add_more()


# Удалить товар из списка
def delete_product_from_list():

    name = input('Введите название товара, который хотите удалить: ').upper()
    del quantity_product[name]
    del price_product[name]

    print(f'Товар «{name}» успешно удалён!')
    print('\nЧто сделать дальше?\n1. Удалить ещё один товар\n2. Выйти в главное меню\n')

    match input('Введите цифру: '):
        case '1':
            delete_product_from_list()
        case '2':
            go_to_menu()
        case _:
            print('Упс, кажется ты не соблюдаешь правила :(\nК сожалению, я вынужден завершить программу')
            sys.exit()


# Посчитать сумму всех товаров с учётом количества каждой единицы
def calculate_cost_products():

    summa = 0
    for name, values in quantity_product.items():
        summa = summa + values * price_product[name]
    print(f'Стоимость всех товаров: {summa}')
    print('Что сделать дальше?\n1. Добавить ещё один товар\n2. Выйти в главное меню\n')

    match input('Введите цифру: '):
        case '1':
            add_product()
        case '2':
            go_to_menu()
        case _:
            print('Упс, кажется ты не соблюдаешь правила :(\nК сожалению, я вынужден завершить программу')
            sys.exit()


# Вызов меню
def call_menu():

    match input('Введите цифру: '):
        case '1':
            view_all_products()
        case '2':
            add_product()
        case '3':
            delete_product_from_list()
        case '4':
            calculate_cost_products()
        case '5':
            sys.exit()
        case _:
            print(f'Упс, кажется ты не соблюдаешь правила :(\n')
            go_to_menu()


def go_to_menu():

    print(f'1. Посмотреть список товаров\n2. Добавить товар\n3. Удалить товар')
    print(f'4. Посчитать сумму товаров\n5. Завершить программу\n')

    match input('Введите цифру: '):
        case '1':
            view_all_products()
        case '2':
            add_product()
        case '3':
            delete_product_from_list()
        case '4':
            calculate_cost_products()
        case '5':
            sys.exit()
        case _:
            print(f'\nУпс, кажется ты не соблюдаешь правила :(\n')
            go_to_menu()

# Старт программы

print('Добро пожаловать!\nЭто программа для учёта товаров.', end=' ')
print(f'Для управления введите цифру, которая соответствует одной из следующих команд:\n')

go_to_menu()

my_list = ['a', 'b', [1, 2, 3], 'd']

# Перебираем элементы списка
for element in my_list:
    # Проверяем, является ли элемент списком
    if isinstance(element, list):
        # Если элемент является списком, перебираем его элементы
        for sub_element in element:
            # Проверяем, является ли элемент цифрой
            if isinstance(sub_element, int):
                print(sub_element)  # Выводим цифру
    # Проверяем, является ли элемент цифрой
    elif isinstance(element, int):
        print(element)  # Выводим цифру

from data_create import name_data, surname_data, phone_data, address_data       # импортируем функции из дата-креатив     


first = 'data_first_variant.csv'
second = 'data_second_variant.csv'

def delete_data():
    file_name = input('Введите имя файла, из которого нужно удалить данные: ')
    with open(first, 'r', encoding='utf-8') as f:
        data = f.readlines()
    with open(second, 'r', encoding='utf-8') as f:
        data = f.readlines()

    print('Текущие данные:')
    print(*data)

    index_to_delete = int(input('Введите номер строки для удаления: ')) - 1
    if 0 <= index_to_delete < len(data):
        del data[index_to_delete]

        with open(first, 'w', encoding='utf-8') as f:
            f.writelines(data)
        with open(second, 'w', encoding='utf-8') as f:
            f.writelines(data)
        print('Данные успешно удалены!')
    else:
        print('Неверный номер строки.')


# delete_data()
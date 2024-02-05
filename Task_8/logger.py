from data_create import name_data, surname_data, phone_data, address_data       # импортируем функции из дата-креатив     



def input_data():
    name = name_data()
    surname = surname_data()
    phone = phone_data()
    address = address_data()
    var = int(input(f'В каком формате записать данные?\n\n'
                    f'1 вариант:\n'
                    f'{name}\n{surname}\n{phone}\n{address}\n\n'
                    f'2 вариант: \n'
                    f'{name};{surname};{phone};{address}\n'
                    f'Выберите вариант: '))
    
    while var != 1 and var != 2:
        print('Неправильный ввод')
        var = int(input('Введите число '))


    if var == 1:
        with open('data_first_variant.csv', 'a', encoding='utf-8') as f:      # открываем фаил для записи контакта
            f.write(f'{name}\n{surname}\n{phone}\n{address}\n\n')       # записываем/сохраняем в файл
    elif var == 2:
        with open('data_second_variant.csv', 'a', encoding='utf-8') as f:      # открываем фаил для записи контакта
            f.write(f'{name};{surname};{phone};{address}\n\n')



def print_data():
    print('Вывожу данные из 1 файла: \n')
    with open('data_first_variant.csv', 'r', encoding='utf-8') as f:      # r -читаем файл
        data_first = f.readlines()      # читаем
        data_first_list = []        # созд где храним
        j = 0
        for i in range(len(data_first)):
            if data_first[i] == '\n' or i == len(data_first) - 1:
                data_first_list.append(''.join(data_first[j:i+1]))      #если верно усл, то добавляем в нашу запись
                j = i
        print(''.join(data_first_list))

    print('Вывожу данные из 2 файла: \n')
    with open('data_second_variant.csv', 'r', encoding='utf-8') as f:
        data_second = f.readlines()
        print(*data_second)
        

# 


# input_data()
# print_data()
# delete_data()





#     filename = 'data_first_variant.csv' if var == 1 else 'data_second_variant.csv'

#     with open(filename, 'a', encoding='utf-8') as f:
#         f.write(f'{name}\n{surname}\n{phone}\n{address}\n\n')

# def print_data():
#     for file_number in range(1, 3):
#         filename = f'data_{file_number}_variant.csv'
#         print(f'Вывожу данные из файла {filename}:')
#         with open(filename, 'r', encoding='utf-8') as f:
#             data = f.read()
#             print(data)
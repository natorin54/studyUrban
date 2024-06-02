print('Работа со словарями.')
my_dict = { 'Nick': 1996, 'Vasya': 1983, 'Petya': 2005, 'Kate': 1994, 'Vera': 1998, 'Liza': 2003}
print('Словарь: ', my_dict)
print('Год рождения Пети: ', my_dict['Petya'])
print('Год рождения Ольги: ', my_dict.get('Olga', 'Такого имени не найдено'))
my_dict['Olga'] = 1987
my_dict['Yura'] = 1976
data_ = my_dict.pop('Vasya')
print('Значение из ячейки "Вася": ', data_)
print('Итоговый словарь: ', my_dict)

print()
print('Работа с множествами.')
my_set = {'lesson', 1, 2, 'lesson', 24, 67, 2, True, 'lesson2', 67, False, True}
print('Множество: ', my_set)
my_set.add(56)
my_set.discard(True)
print('Множество после изменений: ', my_set)

immutable_var = (1, 2.6, 'привет', True)
print(immutable_var)
#immutable_var[1] = 6  - кортеж не поддерживает изменение элементов, кроме случаев, когда элементом кортежа является список

mutable_list = ['Я', 'пока не знаю как', 'программировать', 'на', 'Python']
print(mutable_list)
mutable_list[1] = 'учусь'
print(mutable_list)
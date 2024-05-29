example = str(input())
middle = len(example) // 2
print("Первый символ: " + example[0])
print("Последний символ: " + example[-1])
print("Вторая половина строки: " + example[middle:])
print("Слово наоборот: " + example[::-1])
print("Каждый второй символ строки: " + example[1::2])

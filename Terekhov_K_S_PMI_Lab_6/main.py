import random

from sortedcontainers import SortedSet
from collections.abc import Hashable
print('''1. Создаем множество a_set, содержащее не менее 7 элементов любых разрешенных типов, с помощью 3 – генератора.''')
a_set = {x**2 for x in range(7)}
print(f'Элементы множества a_set: {a_set}')

print('''2. Создает итерабельный объект it_ob, содержащий не менее трех элементов, имеющихся в объекте a_set, и проверить, 
все ли элементы it_ob хэшируемы. Если нет – заменить нехэшируемые элементы хэшируемыми.''')
it_ob = ['d', 'e', [9.5, 17.3], {'abc', 'dbe'}]
# сначала добавляю три элемента из множества
a_set_sort = SortedSet(a_set)
for i in range(3):
    it_ob.append(a_set_sort[random.randint(0, len(a_set) - 1)])
print(f'Элементы it_ob: {it_ob}')
# теперь проверяю хэшируемы ли они

for index, item in enumerate(it_ob):
    if isinstance(item, Hashable) == False:
        old_item = it_ob[index]
        it_ob[index] = tuple(item)
        print(f'Преобразуем {old_item} в {it_ob[index]}')
print(it_ob)

print('''3. Преобразует объект it_ob в множество b_set и выполняет над множествами a_set и b_set операцию 3 – difference().''')
b_set = set(it_ob)
print(f'Элементы нового множества b_set {b_set}')
print(f'Множество b_set не содержит {a_set.difference(b_set)} \n')

print('''4. Создает словарь a_dict с помощью 5 – генератора.''')
a_dict = {x: y for x, y in zip('ABCDEF', range(6))}


a_dict = {x: y for x in 'ABC' for y in 'XYZ'}
print(f'Создан словарь: {a_dict}')

print('''5. Выполняет следующие методы словаря a_dict:1 – clear(), 3 – items(), 5 – pop(key[, default)''')
print(f'Результат выполнения метода items(): {a_dict.items()}')
# для выполнения следующего метода выбирался рандомный элемент словаря
print(f'Результат выполнения метода pop(): {a_dict.pop(random.choice(list(a_dict)))}')
print(f'Результат выполнения метода clear(): {a_dict.clear()}')


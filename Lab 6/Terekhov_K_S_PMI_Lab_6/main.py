# 1. Создает множество a_set, содержащее не менее 7 элементов любых разрешенных типов, с помощью (см. колонку "Множество"/"Создание" табл. №1):
#	3 – генератора.
import random

from sortedcontainers import SortedSet
from collections.abc import Hashable

a_set = {x-8 for x in range(10, 20, 2)}
a_set.add(False)
print(f'Элементы множества a_set: {a_set}')

# 2. Создает итерабельный объект it_ob, содержащий не менее трех элементов, имеющихся в объекте a_set,
#    и проверить, все ли элементы it_ob хэшируемы. Если нет – заменить нехэшируемые элементы хэшируемыми.
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

# 3. Преобразует объект it_ob в множество b_set и выполняет над множествами
#    a_set и b_set операции (см. колонку "Множество"/"Операции" табл. №1):
#	3 – difference();

b_set = set(it_ob)
print(f'Элементы нового множества b_set {b_set}')
print(f'Множество b_set не содержит {a_set.difference(b_set)} \n')

# 4. Создает словарь a_dict с помощью (см. колонку "Словарь"/"Создание" табл. №1):
#	5 – генератора.
a_dict = {x: y for x in 'ABC' for y in 'XYZ'}
print(f'Создан словарь: {a_dict}')

# 5. Выполняет следующие методы словаря a_dict (см. колонку "Словарь"/"Методы" табл. №1):
#	1 – clear();
#	3 – items();
#	5 – pop(key[, default);

print(f'Результат выполнения метода items(): {a_dict.items()}')
# для выполнения следующего метода выбирался рандомный элемент словаря
print(f'Результат выполнения метода pop(): {a_dict.pop(random.choice(list(a_dict)))}')
print(f'Результат выполнения метода clear(): {a_dict.clear()}')


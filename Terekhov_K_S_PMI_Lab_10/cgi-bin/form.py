import cgi, cgitb, random, pickle

main_form = cgi.FieldStorage()
def form_post():
    global in_name
    in_name = main_form.getfirst("in_name")
    test = get_test('tests.dat')
    user_dict = {  # Словарь данных тестируемого содержит:
        'name': in_name,  # имя
        'number_test': 0,  # порядковй номер очередного теста
        'tests': [test],  # список переданных тестов
        'answers': [],  # список ответов пользователя
        'points': 0}  # число набранных баллов
    f = open('user.dat', 'wb')
    pickle.dump(user_dict, f)
    f.close()

def get_test (file_name): # Функция считывает из файла file_name тесты
    f= open (file_name, 'rb' ) # и возвращает один из них
    test_list=pickle.load(f)
    f.close()
    test=random.choice(test_list)
    test_list.remove(test)
    f= open ( 'cur_tests.dat' , 'wb' )
    pickle.dump(test_list,f)
    f.close()
    return test

TESTS= [ 'Тест №1. Изменяемые типы данных:' \
'1. кортеж 2. словарь 3. строка;2' ,
'Тест №2. Выполняется только чтение из текстового файла:\n' \
'1. mode=\'\' 2. mode=\'r\' 3. mode=\'r+\';2' ,
'Тест №3. Выполняется удаление существующего файла:\n' \
'1. mode=\'w\' 2. mode=\'w+\' 3. mode=\'a\';2' ,
'Тест №4.В качестве ключа словаря могут быть использованы:\n' \
'1. кортежи 2. числа 3. строки;2' ,
'Тест №5. Модуль mod имеет фукцию func(). При каком подключении модуля' \
'фукция func() будет непосредсвтвенно доступна программе?\n' \
'1. import mod 2. from mod import func 3. from mod import *;2' ]

f= open ( 'tests.dat' , 'wb' )
pickle.dump(TESTS,f)
f.close()
print ( "It/s done" )

form_post()

print('''
    <ul class="flex-outer">
      <li>
      <div id="div"> 
        <button onclick="start()">Тестирование</button>
      </div>
      </li>
    </ul>
    ''')








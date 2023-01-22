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

TESTS= [ 'Тест №1. Множество, не содержащее ни одного элемента, называется:\n' \
'1. Пустым 2. Конечным 3. Нулевым;1' ,
'Тест №2. Правильная запись предложения «Y – множество действительных чисел, больших 3»:\n' \
'1. Y={y|yR, y>3}  2. Y={R| y>3} 3. Y={yR|y>3};3' ,
'Тест №3. Непересекаются множества чисел:\n' \
'1. Простых и четных 2. Простых и нечетных 3.Простых и составных;3' ,
'Тест №4.Мощность множества A={-3,0,2,5,13} равна:\n' \
'1. 5 2. 15 3. 2;1' ,
'Тест №5. Существует ли множество без элементов?\n' \
'1. Нет 2. ДА 3. В любом множесте должен быть хотя бы 1 элемент;2' ]




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








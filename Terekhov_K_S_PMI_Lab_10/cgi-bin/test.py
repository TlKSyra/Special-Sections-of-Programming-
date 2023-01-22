print ( "Access-Control-Allow-Origin: *" )
print ()
import cgi, cgitb, random, pickle
cgitb.enable()
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


def write_results (user_dict, out_points=0, out_answers=0):
    print ('<i><b>Результаты тестирования:</b></i>' ,
    '<br>Имя &ndash; ' , user_dict[ 'name' ])
    if out_points:
        print ( '<br>Получено баллов &ndash; ' ,
        user_dict['points'], ' из ' , user_dict[ 'number_test' ])

    if out_answers:
        print ( '<br>Ответы &ndash; ' )
        for el in user_dict[ 'answers' ]: print (el)
        print ( '<br>Оценка &ndash; ' )
    m=user_dict[ 'points' ]
    if m==0: mark= "Неудовлетворительно"
    elif m==1: mark= "Удовлетворительно"
    elif m==2: mark= "Хорошо"
    else : mark= "Отлично"
    print ( '"' , mark, '"' )

max_test = 4
data = cgi.parse()

if 'start' in data:
    f = open('user.dat', 'rb')
    user_dict = pickle.load(f)
    test = get_test('cur_tests.dat')
    print('''<button name="''' + test.split(';')[0] + '''" id="test" onclick="subm1()">Answer the ''' + str(user_dict[
        'number_test'] + 1) + ''' question</button><br><br>''')
    user_dict['number_test'] += 1
    user_dict['tests'] += [test]
    f = open('user.dat', 'wb')
    pickle.dump(user_dict, f)
    f.close()
if 'answer' in data:
	f= open ( 'user.dat' , 'rb' )
	user_dict=pickle.load(f)
	user_dict[ 'answers' ]+=[data[ 'answer' ][0]]
	tests=user_dict[ 'tests' ]
	etalon= tests[ len (tests)-1:][0].split( ';' )[1]
	if etalon == user_dict['answers'][user_dict['number_test']-1]:
		user_dict['points'] += 1
	if user_dict[ 'number_test' ]<max_test:
		test=get_test( 'cur_tests.dat' )
		print('''<button name="'''+test.split( ';' )[0]+'''" id="test" onclick="subm1()">Answer the '''+ str(user_dict[ 'number_test' ] + 1) +''' question</button><br><br>''')
		user_dict[ 'number_test' ]+=1
		user_dict[ 'tests' ]+=[test]
		f= open ( 'user.dat' , 'wb' )
		pickle.dump(user_dict,f)
		f.close()
	else :
		write_results(user_dict,out_points=1,out_answers=1)

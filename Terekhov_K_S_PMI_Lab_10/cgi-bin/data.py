import random, pickle
def get_test (): # Функция считывает из файла file_name тесты
    f= open ('cur_tests.dat', 'rb' ) # и возвращает один из них
    test_list=pickle.load(f)
    f.close()
    test=random.choice(test_list)
    test_list.remove(test)
    f= open ( 'cur_tests.dat' , 'wb' )
    pickle.dump(test_list,f)
    f.close()
    return test

print(get_test())
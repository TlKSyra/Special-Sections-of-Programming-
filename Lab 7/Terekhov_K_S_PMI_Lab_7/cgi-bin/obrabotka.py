#! /usr/bin/python3
import cgi, sys
import os.path
from datetime import datetime

main_form = cgi.FieldStorage()
sys.stdout.buffer.write(b'Content-type: text/html;charset=utf-8\n\n')


def form_post():
    # принимаем данные из формы
    global in_name, in_faculty, in_email
    in_name = main_form.getfirst("in_name")
    in_faculty = main_form.getfirst("in_faculty")
    in_email = main_form.getfirst("in_email")

# создаем директорию
def create_dir_and_files():
    try:

        if os.path.exists('CGI'):
            print("Папка CGI уже создана")
        else:
            os.mkdir('CGI')
            print("Создана папка CGI")

        with open('./CGI/names.txt','a') as names:
            nm = [f'Время добавления:{datetime.strftime(datetime.now(), "%d/%m/%Y %H:%M")}\n',
                  f'ФИО: {in_name}\n']
            names.writelines(nm)
            names.close()
        with open('./CGI/values.txt', 'a') as values:
            values.write(f'Время добавления:{datetime.strftime(datetime.now(), "%d/%m/%Y %H:%M")} ')
            values.write(f'ФИО: {in_name} ')
            values.write(f'Факультет: {in_faculty} ')
            values.write(f'Электронная почта: {in_email} ')
            values.close()

        with open('./CGI/binary_data.dat', 'wb') as binary_data:
            # создадим последовательность чисел длиной в 14
            binary_data.write(bytes(range(14)))
            binary_data.close()
    except Exception as e:
        print(f'Ошибка: {e}')

def get_size():
    try:
        global file_names_size
        global file_values_size
        file_names_size = os.path.getsize('./CGI/names.txt')
        file_values_size = os.path.getsize('./CGI/values.txt')
    except Exception as e:
        print((f'Ошибка: {e}'))

def read_file():
    file = open('./CGI/values.txt', 'r')
    return file.readlines()

def value_byte():
    file = open('./CGI/binary_data.dat', 'rb')
    global int_val
    global offset_value
    global last_val
    global msg
    msg = ""
    data = file.read()
    int_val = (data[8].to_bytes(2, byteorder="big"))
    last_val = data[-1]
    try:
        assert (str(last_val)[1] == 5)
        msg = "Предположение верно, последовательность заканчивается на три."
    except AssertionError:
        msg = f'Неверно. Последовательность не заканчивается на три.'
    file.seek(10,0)
    three_byres_offset = file.read(3)
    offset_value = ', '.join(str((data[i]).to_bytes(2, byteorder="big")) for i in three_byres_offset)
    return int_val, offset_value, msg

def get_script():
    print("""<!DOCTYPE HTML>
        <html>
        <head>
            <meta charset = "utf-8">
            <title>Результат</title>
            <link rel="stylesheet" media="screen" href="styles.css" >
        </head>
        <body>
        <div id ="input_result"> """)
    print(f"""
        <p class='greet'>Добрый день, <span class='name'><strong><i>{in_name}!</i></strong></span></p><br>
        <p>Длина файла names.txt равна <b>{file_names_size} bytes</b></p>
        <p>Длина файла values.txt равна <b>{file_values_size} bytes</b></p>
        <p>Содержание файла <i>values.txt</i>:</p>
        <textarea id="text_from_file" readonly>{read_file()}></textarea>
        <p>Значение байта под номером 8: <b>{int_val}</b></p>
        <p>Значение 3 байтов после смещения на 10: <b>{offset_value}</b></p>
        <p>Заканчивается ли последовательность на 5? <b>{msg}</b></p> """)


def main():
    form_post()
    if (in_name == None) or (in_faculty == None) or (in_email == None):
        print("Введенные вами данные некорректны. Попробуйте снова.")
    else:
        create_dir_and_files()
        get_size()
        value_byte()
        get_script()

main()


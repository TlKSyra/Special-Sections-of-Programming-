#! /usr/bin/python3
import cgi, sys
from random import randrange

main_form = cgi.FieldStorage()


def form_post():
    global in_name, select_func1, select_func2, select_func3
    in_name = main_form.getfirst("in_name")
    select_func1 = main_form.getfirst("select_func1")
    select_func2 = main_form.getfirst("select_func2")
    select_func3 = main_form.getfirst("select_func3")

def get_list():
    global num, abs_num
    num = []
    for i in range(12):
        num.append(randrange(-4, 3, 1))

def get_data1():
    global data1
    if select_func1 == "выполнить":
        product = 1
        for n in num:
            if n % 2 != 0:
                product *= n
        data1 = f'Произведение нечетных чисел списка: {product}.'
    else:
        data1 = f'Функция данной группы не выполнялась.'

def get_data2():
    global data2
    if select_func2 == "выполнить":
        new_num = []
        for n in num:
            if n > 0:
                new_num.append(n)
        data2 = f'Минимальное число в списке среди положительных: {min(new_num)}.'
    else:
        data2 = f'Функция данной группы не выполнялась.'

def get_data3():
    global data3
    if select_func3 == "выполнить":
        new_num = num.copy()
        new_num.sort(key=lambda x: x % 3)
        data3 = f'Отсортированный список по модулю 3: {new_num}.'
    else:
        data3 = f'Функция данной группы не выполнялась.'

def main():
    form_post()
    get_list()
    get_data1()
    get_data2()
    get_data3()

main()

print("Content-type: text/html\n")
print("""<!DOCTYPE HTML>
        <html>
        <head>
            <meta charset = "utf-8">
            <title>Результат</title>
            <link rel="stylesheet" href="/styles/stylesnew.css" >
        </head>
        <body>
        <div id ="input_result" class="container"> """)
print(f"""
            <p>Добрый день, <b>{in_name}</b>! Взгляните на результат работы.</p>
            <p>Список чисел: <b>{num}</b></p>
            <p>Группа 1. <b>{data1}</b></p>
            <p>Группа 2. <b>{data2}</b></p>
            <p>Группа 3. <b>{data3}</b></p>
        </div>
        </body>
        </html> """)

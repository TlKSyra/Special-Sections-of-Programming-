#! /usr/bin/python3
import cgi, sys
import re

main_form = cgi.FieldStorage()


def form_post():
    global in_name, in_faculty, number_credit_book, in_literal
    in_name = main_form.getfirst("in_name")
    in_faculty = main_form.getfirst("in_faculty")
    number_credit_book = main_form.getfirst("number_credit_book")
    in_literal = main_form.getfirst("in_literal")

def get_data1():
    global data1_resp
    data1_regex = re.compile(r"^(Студ.)\s([a-zA-Za-яА-Я0-9]+)\s(ф_т)\s([a-zA-Za-яА-Я0-9]+)$")
    data1_s = data1_regex.search(in_faculty)
    if data1_s:
        data1_resp = 'data1 соответствует схеме "Студ. {} ф_т {}"'
    else:
        data1_resp = 'data1 не соответствует схеме "Студ. {} ф_т {}"'


def get_data2():
    global data2_resp
    data2_m = re.match(r"^(Фамилия И. О.)\s([a-zA-Za-яА-Я0-9]+)\s\D{1}. \D{1}[.]$", in_name)
    if data2_m:
        data2_resp = 'data2 соответствует схеме "Фамилия И.О. {}"'
    else:
        data2_resp = 'data2 не соответствует схеме "Фамилия И.О. {}"'


def get_data3():
    global data3_resp
    data3_s = re.search(r"^(Номер ЗК)\s\d{7}$", number_credit_book)
    if data3_s:
        data3_resp = 'data3 соответствует схеме "Номер ЗК {}"'
    else:
        data3_resp = 'data3 не соответствует схеме "Номер ЗК {}"'


def get_data4():
    global data4_resp
    data4_regex = re.compile(r"^{\".+\"\s:\s\".+\",\s\d+\s:\s\d+.\d+}$")
    data4_m = data4_regex.match(in_literal)
    if data4_m:
        data4_resp = 'data4 соответствует схеме "{"str" : "str", int : float}"'
    else:
        data4_resp = 'data4 не соответствует схеме "{"str" : "str", int : float}"'


def get_script():
    sys.stdout.buffer.write(b'Content-type: text/html;charset=utf-8\n\n')


def main():
    form_post()
    get_data1()
    get_data2()
    get_data3()
    get_data4()

main()

print("Content-type: text/html\n")
print("""<!DOCTYPE HTML>
        <html>
        <head>
            <meta charset = "utf-8">
            <title>Результат</title>
            <link rel="stylesheet" href="/styles.css" >
        </head>
        <body>
        <div id ="input_result" class="container"> """)
print(f"""
            <p>{in_faculty} - <b>{data1_resp}</b></p>
            <p>{in_name} - <b>{data2_resp}</b></p>
            <p>{number_credit_book} - <b>{data3_resp}</b></p> 
            <p>{in_literal} - <b>{data4_resp}</b></p>
        </div>
        </body>
        </html> """)

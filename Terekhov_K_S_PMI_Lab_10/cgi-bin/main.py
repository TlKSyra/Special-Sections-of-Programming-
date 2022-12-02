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


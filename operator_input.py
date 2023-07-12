from work_with_file import fields
from work_with_menu import find_index_by_number

def get_search_name():
    return input("Введите фамилию\n").strip()

def get_search_number():
    return input("Введите номер телефона\n").strip()

def get_new_user():
    user = dict()
    for field in fields():
        user[field] = input(field + "\n")
    return user

def change_user(phone_book):
    index = find_index_by_number(phone_book, get_search_number())
    if index < 0:
        print("Абонент не найден")
        return False, phone_book
    print("Введите новые данные абонента")
    return True, change_record(phone_book, index, get_new_user())

def change_record(phone_book, index, record):
    return phone_book[:index] + [record] +  phone_book[index + 1:]
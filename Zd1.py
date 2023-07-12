
from work_with_file import (read_csv, write_phonebook, get_file_name, write_txt)
from work_with_menu import (show_menu, print_result, print_serch_result, find_by_name, find_by_number, add_user, del_user, find_index_by_number, change_user)
from operator_input import (get_search_name, get_search_number, get_new_user)


def work_with_phonebook():
    choice = show_menu()
    phone_book = read_csv('phonebook.csv')

    while (choice != 0):
        if choice == 1:
            print_result(phone_book)
        elif choice == 2:
            name = get_search_name()
            print_serch_result(find_by_name(phone_book, name))
        elif choice == 3:
            number = get_search_number()
            print_serch_result(find_by_number(phone_book, number))
        elif choice == 4:
            user_data = get_new_user()
            add_user(phone_book, user_data)
            write_phonebook(phone_book)
        elif choice == 5:
            number = get_search_number()
            modified, phone_book = del_user(phone_book, find_index_by_number(phone_book, number))
            if modified:
                write_phonebook(phone_book)
        elif choice == 6:
            modified, phone_book = change_user(phone_book)
            if modified:
                write_phonebook(phone_book)
        elif choice == 9:
            file_name = get_file_name()
            write_txt(file_name, phone_book)
        choice = show_menu()

work_with_phonebook()
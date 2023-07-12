def show_menu():
    print("\nВыберите необходимое действие:",
          ("1") + ". Отобразить весь справочник",
          ("2") + ". Найти абонента по фамилии",
          ("3") + ". Найти абонента по номеру телефона",
          ("4") + ". Добавить абонента в справочник",
          ("5") + ". Удалить абонента по номеру телефона",
          ("6") + ". Изменить абонента по номеру телефона",
          ("9") + ". Сохранить справочник в текстовом формате",
          ("0") + ". Закончить работу",
          sep="\n")
    choice = int(input())
    return choice

def print_result(phone_book):
    temp = list(map(lambda x: [x[0] + 1] + [y for y in x[1].values()], list(enumerate(phone_book))))
    for i in temp:
        print(i)
    
def print_serch_result(search_result):
    print_result(search_result) if search_result else print("Абонент не найден")

def find_by_name(phone_book, name):
    return find_by_field(phone_book, "Фамилия", name)

def find_by_number(phone_book, number):
    return find_by_field(phone_book, "Телефон", number)

def find_by_field(phone_book, field, value):
    result = []
    for record in phone_book:
        if record[field].lower() == value.lower():
            result.append(record)
    return result

def find_index_by_number(phone_book, number):
    return find_index_by_field(phone_book, "Телефон", number)

def find_index_by_field(phone_book, field, value):
    for index in range(len(phone_book)):
        if phone_book[index][field].lower() == value.lower():
            return index
    return -1

def add_user(phone_book: list, user_data):
    phone_book.append(user_data)

def del_user(phone_book: list, index: int):
    if index < 0:
        print("Абонент не найден")
        return False, phone_book
    return True, phone_book[:index] + phone_book[index + 1:]
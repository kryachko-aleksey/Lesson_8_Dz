

def write_csv(filename: str, data: list):
    with open(filename, 'w', encoding='utf-8') as fout:
        for i in range(len(data)):
            s = ''
            for v in data[i].values():
                s += v + ','
            fout.write(f'{s[:-1]}\n')

def read_csv(filename: str) -> list:
    data = []
    with open(filename, 'r', encoding='utf-8') as fin:
        for line in fin:
            record = dict(zip(fields(), line.strip().split(',')))
            data.append(record)
    return data

def write_phonebook(phone_book):
    write_csv('phonebook.csv', phone_book)

def fields():
    return ["Фамилия", "Имя", "Телефон", "Описание"]    

def get_file_name():
    return "phon.txt"

def write_txt(filename: str, data: list):
    write_csv(filename, data)
# СЛОВАРИ
'''
# создание
my_dict = {}
ex_dict = dict()

dict_1 = {"ключ_1": "значение_1", "ключ_2": 2, "ключ_3": [1, 3, 5]}
dict_2 = {1: "значение_1", 2: "значение_2", 3: "значение_3"}
dict_3 = {"name": "Ivan", "age": 20, "lang": ["ru", "en", "jap"]}

new_d_2 = dict(fruits=["apple", "banana", "mango"], vegetables={"tomato", "potato", "paprika"})

new_d = {f"ключ_{i}": f"значение_{i}" for i in range(0, 10)}

print(dict_2)
print(new_d_2)
print(new_d)

# обращение к элементам
# dict_2 = {1: "значение_1", 2: "значение_2", 3: "значение_3"}

print(dict_2[1])
# print(dict_2[0])
print(dict_2.get(0))
print(dict_2.get(0, 0))

dict_2[4] = "новое_значение"
dict_2[1] += "_поменяли"
print(dict_2)

# del dict_2[2]
dict_2.pop(2)
print(dict_2)

# методы
print(list(dict_2.keys()))
print(dict_2.values())
dict_2.update({"2": "новый_словарь", 6: ""})
print(dict_2)

try:
    dict_2[2]
except KeyError as e:
    print(f"Ошибка: Ключ {e} не найден")
'''
# РЕГУЛЯРНЫЕ ВЫРАЖЕНИЯ
import re
# основные методы                                           # ещё методы
'''
re.search(pattern, string) - поиск первого совпадения       re.match(pattern, string) - поиск совпадения только в начале строки
re.findall(pattern, string) - поиск всех совпадений         re.fullmatch(pattern, string) - проверка на соответствие всей строки
re.sub(pattern, new_str, string) - замена                   re.finditer(pattern, string) - как .findall, но возвращает итератор объектов
re.split(pattern, string) - разделение                      re.compile(pattern) - сборка регулярного выражения в отдельный объект
'''
# базовый синтаксис                                         # флаги
'''
. - любой символ кроме новой строки                         re.IGNORECASE / re.I 
^ - начало строки                                           re.MULTILINE / re.M
$ - конец строки                                            re.DOTALL / re.S
* - 0 или более повторений
+ - 1 или более повторений                                  # методы объектов match()
| - ИЛИ
? - 0 или 1 повторение                                      .group() - возвращает найденную строку
\d - любая цифра                                            .groups() - возвращает кортеж всех найденных групп
\w - любая буква, цифра или "_"                             .start() - возвращает индекс начала совпадения
\s - пробельный символ                                      .end() - возвращает индекс конца совпадения
[a-zA-Z] - набор символов                                   .span() - возвращает кортеж (start, end)
'''
text = ("ФИО: Иванов Иван Иванович;"
        "возраст: 33 года;"
        "почта: email@example.com, email_2@ex.ru;"
        "номер телефона: +7(900)555-35-35, 8(800)555-35-35.")
# text = "ФИО: Иванов Иван Иванович; возраст: 33 года; почта: email@example.com, email_2@ex.ru; номер телефона: +7(900)555-35-35, 8(800)555-35-35."

email_1 = re.search(r'[\w.-]+@[\w]+[.com]*[.ru]*', text).group()
print(email_1)
email_all = re.findall(r'[a-zA-Z\d.-]+@[\w]+[.com]*[.ru]*', text)
print(email_all)
email_all = re.sub(r'[a-zA-Z]+[\w.-]+@[\w.-]+[.com]*[.ru]*', "-"*10, text)
print(email_all)
str_split = re.split(r'[+()-]+', "+7(900)555-35-35")
print(str_split)

# Перепиши из памяти (не подсматривая!), что делают эти методы:
# .append() — добавляет в конец
# .extend() — добавляет несколько
# .remove() — удаляет
# .pop() — удаляет все и возвращает последний


# Потом проверь себя, запустив этот код:
test_list = [1, 2, 3]
test_list.append(4)
print("После append:", test_list)

test_list.extend([5, 6])
print("После extend:", test_list)

# Реши эти ПРОСТЫЕ задачи (легче, чем были):

# 1. Дан список чисел. Выведи каждое число
numbers = [10, 20, 30]
for num in numbers:
    print(num)  # Запусти, посмотри результат

# 2. Дан список имён. Выведи каждое имя
names = ["Alice", "Bob", "Charlie"]
for name in names:
    print(name)

# 3. Дан словарь. Выведи каждый ключ и значение
person = {"name": "Tom", "age": 24}
print(person.items())
for key, value in person.items():
    print(key, value)  # Запусти, посмотри результат


students = [("Alice", 85), ("Bob", 92)]
for name, score in students:  # Достаёшь name и score из каждого кортежа
    print(name, "получил", score)


# Упрощённая версия задачи 11
# Дан список словарей с пользователями
users = [
    {"name": "Alice", "age": 25},
    {"name": "Bob", "age": 17},
    {"name": "Charlie", "age": 30}
]

# Выведи имена всех пользователей
# for user in users:
#     print(user["name"])

for user in users:
    if user['age'] > 18:
        print(user['name'])

# Теперь выведи только тех, кто старше 18
# (Попробуй сам, если не получится — напиши, разберём вместе)
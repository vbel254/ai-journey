
# ЗАДАЧА 1: Базовые операции
# Создай список из 5 любых чисел. Добавь в конец число 10, 
# затем вставь на 2-ю позицию (индекс 1) число 99.
# Выведи итоговый список.

my_list = [2, 5, 4, 0]

my_list.append(10)

my_list.insert(1, 99)

print(my_list)


# ЗАДАЧА 2: Срезы (slicing)
# Дан список: days = ['Пн', 'Вт', 'Ср', 'Чт', 'Пт', 'Сб', 'Вс']
# Получи: а) первые 5 дней, б) выходные, в) каждый второй день
days = ['Пн', 'Вт', 'Ср', 'Чт', 'Пт', 'Сб', 'Вс']
weekdays = days[0:5]
weekend = days[5:7]
every_second = days[1::2]

print(weekdays)
print(weekend)
print(every_second)


# ЗАДАЧА 3: Методы списков
# Дан список: scores = [85, 92, 78, 92, 65, 92]
# а) Удали первое вхождение 92
# б) Посчитай, сколько раз встречается 92 (используй метод .count())
# в) Найди индекс числа 78 (используй метод .index())
scores = [85, 92, 78, 92, 65, 92]

scores.remove(92)
print(scores)

print(scores.count(92))

print(scores.index(78))


# ЗАДАЧА 4: Создание и распаковка
# Создай кортеж с координатами (широта=55.75, долгота=37.61)
# Распакуй его в переменные lat и lon. Выведи их.

coordinates = (55.75, 37.61)

lat, lon = coordinates

print(lat, lon)


# ЗАДАЧА 5: Кортеж как ключ словаря
# Создай словарь, где ключи — координаты (кортежи), 
# значения — названия мест. Например: (0, 0): "Старт"
# Добавь минимум 3 точки.

coordinates_5 = {
    (0, 0): "Старт",
    (2, 4): "Поворот",
    (5, 7): "Финиш",
}

print(coordinates_5)

print(coordinates_5.keys())
print(coordinates_5.values())
print(coordinates_5.items())


# ЗАДАЧА 6: Создание и изменение
# Создай словарь с информацией о студенте:
# имя, возраст, курс (год обучения), средний балл
# Измени средний балл на 4.5 и добавь ключ "университет"

student = {
    'name': 'Tom',
    'age': 24,
    'year_study': 2026,
    'middle_score': 1.99
}

student['middle_score'] = 4.5
student['university'] = 'Stenford'

print(student)


# ЗАДАЧА 7: Методы словаря
# Дан словарь: prices = {"apple": 50, "banana": 30, "orange": 45}
# а) Получи список всех товаров (keys)
# б) Получи список всех цен (values)
# в) Проверь, есть ли товар "grape" (используй 'in')
prices = {"apple": 50, "banana": 30, "orange": 45}

print(prices.keys())
print(prices.values())

if 'grape' in prices:
    print('Yes')
else:
    print('No')


# ЗАДАЧА 8: ML-кейс — конфигурация модели
# Создай словарь model_config с параметрами:
# learning_rate: 0.001, batch_size: 32, epochs: 10
# Увеличь epochs в 2 раза. Выведи финальную конфигурацию.

model_config = {
    'learning_rate': 0.001,
    'batch_size': 32,
    'epochs': 10
}

model_config['epochs'] *= 2

print(model_config)


# ЗАДАЧА 9: Удаление дубликатов
# Дан список: numbers = [1, 2, 2, 3, 4, 4, 4, 5, 1]
# Преобразуй в множество, чтобы удалить дубликаты.
# Затем преобразуй обратно в отсортированный список.

numbers = [1, 2, 2, 3, 4, 4, 4, 5, 1]

unique_numbers = set(numbers)
print(unique_numbers)

numbers = sorted(unique_numbers)
print(numbers)


# ЗАДАЧА 10: Операции с множествами
# Даны два множества студентов:
# python_students = {"Alice", "Bob", "Charlie", "David"}
# ml_students = {"Charlie", "David", "Eve", "Frank"}
# Найди: а) кто изучает оба курса, б) только Python, в) хотя бы один курс

python_students = {"Alice", "Bob", "Charlie", "David"}
ml_students = {"Charlie", "David", "Eve", "Frank"}

both_courses = python_students & ml_students
print("Оба курса:", both_courses)

only_python = python_students - ml_students
print("Только Python:", only_python)

difference_ml = ml_students - python_students
print(difference_ml)

at_least_one = python_students | ml_students
print("Хотя бы один:", at_least_one)


# ЗАДАЧА 11: Список словарей (важно для ML!)
# Создай список из 3 словарей, каждый описывает пользователя:
# ключи: name, age, city
# Выведи имена всех пользователей старше 20 лет (используй обычный цикл for)

users = [
    {'name': 'Tom', 'age': 34, 'city': 'NY'},
    {'name': 'Gek', 'age': 36, 'city': 'Moscow'},
    {'name': 'Artur', 'age': 2, 'city': 'Moscow'}
]

for user in users:
    if user['age'] > 20:
        print(user['name'])


# ЗАДАЧА 12*: Группировка данных
# Дан список оценок студентов:
# grades = [("Alice", 85), ("Bob", 92), ("Alice", 78), ("Bob", 88)]
# Создай словарь, где ключ — имя студента, значение — список его оценок
# Результат: {"Alice": [85, 78], "Bob": [92, 88]}
grades = [("Alice", 85), ("Bob", 92), ("Alice", 78), ("Bob", 88)]
# Подсказка: используй цикл for и метод .get() или .setdefault()

result = {}

for name, grade in grades:
    if name not in result:
        result[name] = []
    result[name].append(grade)

print(result)


# Эксперимент 1
list1 = [1, 2, 3]
list1.append([4, 5])
print(list1)  # Что будет?

# Эксперимент 2
list2 = [1, 2, 3]
list2.extend([4, 5])
print(list2)  # Что будет?
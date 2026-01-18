# Дано:
model_name = "GPT-Mini"
parameters = "1500000000"  # параметры модели (строка!)
accuracy = "94.7"           # точность в % (строка!)
is_open_source = "True"     # (строка!)

# ТВОЯ ЗАДАЧА:
# 1. Преобразуй parameters в int и сохрани в переменную params_int

params_int = int(parameters)
print(params_int)
print(type(params_int))

# 2. Преобразуй accuracy в float и сохрани в переменную acc_float

acc_float = float(accuracy)
print(acc_float)
print(type(acc_float))

# 3. Преобразуй is_open_source в bool (подсказка: нужно сначала сравнить со строкой "True")

is_open_source = is_open_source == "True"
print(type(is_open_source))

# 4. Выведи красивый отчёт с f-string:
#    "Модель: [название]
#     Параметры: [число] млрд
#     Точность: [число]%
#     Open-source: [True/False]"

print(f'Модель: {model_name}\n'
      f'Параметры: {params_int / 1_000_000_000} млрд\n'
      f'Точность: {acc_float}%\n'
      f'Open-source: {is_open_source}')

# 5. Проверь типы всех переменных через type() и выведи их

print(f'Модель тип: {type(model_name)}\n'
      f'Параметры тип: {type(params_int)}\n'
      f'Точность тип: {type(acc_float)}\n'
      f'Open-source тип: {type(is_open_source)}')

# Дополнительно (*бонус):
# 6. Вычисли сколько миллиардов параметров (раздели params_int на 1_000_000_000)

print(params_int / 1_000_000_000)

# 7. Проверь условие: если точность > 90.0 И open-source = True, выведи "✅ Отличная модель!"

if acc_float > 90.0 and is_open_source:
    print('✅ Отличная модель!')
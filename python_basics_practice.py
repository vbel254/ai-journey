name = 'Tom'
age = 24
learn_ai = True

print(type(name), type(age), type(learn_ai))

print('---')

age = str(age)

print(f'My age is {age} year')
print(type(age))

print('---')

print(47 ** 3, 100 % 7, 100 // 7)

print('---')

a, b = 10, 3

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b)
print(a % b)
print(a ** b)

print('---')

text = "  Python для AI  "

print(text.strip())
text = text.strip()

print(text.upper())
print(text.replace('Python', 'ML'))

day = 1

print(f'Я изучаю Python уже {day} день')

print('---')

temperature = 25

if temperature > 30:
    print('Жарко')
elif 15 <= temperature <= 30:
    print('Комфортно')
else:
    print('Холодно')

print('---')

for i in range(1, 11):
    print(i)

for i in range(2, 21, 2):
    print(i)

s = 0
for i in range(1, 101):
    s += i
print(s)

print('---')

def square(x):
    return x ** 2
print(square(2))

def is_even(n):
    return n % 2 == 0
print(is_even(4))
print(is_even(5))

def greet(name, age=18):
    return f'Привет, {name}! Тебе {age} лет'
print(greet('Tom'))
print(greet('Tom', 21))

print('---')

secret = 7

while True:
    number = int(input('Загадай число от 1 до 10:'))

    if number == secret:
        print('Правильно!')
        break
    elif number > secret:
        print('Слишком много')
    else:
        print('Слишком мало')
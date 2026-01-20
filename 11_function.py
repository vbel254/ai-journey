# ЗАДАЧА 1


def calculate_tokens(text):
    return len(text.split())


# Проверка:
result = calculate_tokens("Привет мир Python")
print(result)  # Должно быть 3


# ЗАДАЧА 2
def clean_text(text):
    return text.strip().lower()


# Проверка:
print(clean_text("  HELLO World  "))  # "hello world"


# ЗАДАЧА 3
def combine_texts(*texts):
    return " ".join(texts)


# Проверка:
print(combine_texts("AI", "is", "cool"))  # "AI is cool"
print(combine_texts("GPT", "Claude"))  # "GPT Claude"


# ЗАДАЧА 4 *args
text_lengths = [23, 67, 45, 120, 89, 12, 55]

# Твой код с lambda здесь:
long_texts = list(filter(lambda x: x > 50, text_lengths))

print(long_texts)  # [67, 120, 89, 55]

# numbers = [1, 2, 3, 4]
# doubled = list(map(lambda x: x * 2, numbers))
# print(doubled)  # [2, 4, 6, 8]


# ФИНАЛЬНАЯ ЗАДАЧА **kwargs
def create_dataset_config(**kwargs):
    kwargs["created"] = "2026-01-19"  # просто добавляем ключ
    return kwargs


# def create_dataset_config(**kwargs):
#     return kwargs | {"created": "2026-01-19"}

# Проверка:
config = create_dataset_config(source="csv", size=1000, shuffle=True)
print(config)
# Должно быть: {'source': 'csv', 'size': 1000, 'shuffle': True, 'created': '2026-01-19'}

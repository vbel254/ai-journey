# text = "  Hello World!  "

# # Очистка пробелов
# text.strip()      # "Hello World!"
# text.lower()      # "  hello world!  "
# text.upper()      # "  HELLO WORLD!  "

# # Разбиение и объединение
# text.split()      # ["Hello", "World!"]
# "-".join(["a", "b"])  # "a-b"

# # Замена
# text.replace("World", "Python")  # "  Hello Python!  "


def clean_text(text):
    text = text.strip().lower().replace('!', '').replace(',', '')
    return text


# Тесты:
print(clean_text("  Hello, World!  "))  # должно быть: "hello world"
print(clean_text("AI is Amazing!!!"))  # должно быть: "ai is amazing"


# Задача 2: Токенизация (разбиение текста на слова)
def tokenize(text):
    text = clean_text(text).split()
    return text


# Тесты:
print(tokenize("  Hello, World!  "))  # ["hello", "world"]
print(tokenize("AI is Amazing!!!"))  # ["ai", "is", "amazing"]
print(tokenize("Python   has    spaces"))  # ["python", "has", "spaces"]


# ФИНАЛЬНАЯ ЗАДАЧА: Частота слов (Word Frequency)
def word_frequency(text):
    text = tokenize(text)  # ["hello", "world", "hello"]
    text_dict = {}
    for word in text:
        if word in text_dict:
            text_dict[word] += 1
        else:
            text_dict[word] = 1
    return text_dict


# Или более питонический способ через .get():
# def word_frequency(text):
#     text = tokenize(text)
#     text_dict = {}
#     for word in text:
#         text_dict[word] = text_dict.get(word, 0) + 1
#     return text_dict


# Тесты:
print(word_frequency("hello world hello"))
# {'hello': 2, 'world': 1}

print(word_frequency("AI is amazing! AI is the future."))
# {'ai': 2, 'is': 2, 'amazing': 1, 'the': 1, 'future': 1}

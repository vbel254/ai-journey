# Нужно:
# 1. Убрать дубликаты предложений
# 2. Токенизировать каждое предложение (разбить на слова)
# 3. Убрать стоп-слова из токенов
# 4. Подсчитать частоту каждого слова (Counter или defaultdict)
# 5. Вернуть топ-5 самых частых слов как список кортежей

# Требования:
# - Использовать set для удаления дубликатов предложений
# - Использовать set для быстрой проверки стоп-слов
# - Использовать dict или Counter для подсчета
# - Учитывать сложность алгоритма (стремиться к O(n))

# Ожидаемый результат:
# [("machine", 4), ("learning", 3), ("deep", 2), ...]

import string
from collections import Counter

# sentences = [
#     "Machine learning is amazing",
#     "Deep learning is a subset of machine learning",
#     "Machine learning is amazing",
#     "AI and machine learning are the future",
#     "Deep learning uses neural networks",
#     "Machine, learning is powerful"
# ]

sentence = input("Введите предложение: ")

# stopwords = {"is", "a", "of", "the", "and", "are"}
stopwords = {}


def process_text(sentence, stopwords):
    # sentences_unique = set(sentences)
    # filtered_words = []
    # for sentence in sentences_unique:
    #     tokens = sentence.lower().translate(str.maketrans('', '', string.punctuation)).split()
    #     filtered_words.extend([word for word in tokens if word not in stopwords])
    punctuation_without_hyphen = string.punctuation.replace('-', '')
    words = (
        sentence.lower()
        .translate(str.maketrans('', '', punctuation_without_hyphen))
        .split()
    )
    filtered_words = [word for word in words if word not in stopwords]
    word_count = Counter(filtered_words)
    top_5 = word_count.most_common(5)
    return top_5


result = process_text(sentence, stopwords)
print("Топ-5 самых частых слов:")
for word, count in result:
    print(f"{word}: {count}")

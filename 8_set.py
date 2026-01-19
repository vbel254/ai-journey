predictions = ["cat", "dog", "cat", "bird", "dog", "cat", "fish", "bird", "snake"]
true_labels = ["cat", "dog", "bird", "bird", "cat", "cat", "fish", "bird", "lizard"]

# Найдёт все уникальные классы в predictions

pred_set = set(predictions)
print(pred_set)

# Найдёт все уникальные классы в true_labels

true_set = set(true_labels)
print(true_set)

# Найдёт классы, которые модель предсказала, но НЕ было в истинных метках

print(pred_set - true_set)

# Найдёт классы, которые были в истинных метках, но модель НЕ предсказала

print(true_set - pred_set)

# Выведет общее количество уникальных классов в обоих списках

print(len(pred_set | true_set))
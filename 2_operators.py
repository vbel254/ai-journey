# Данные модели машинного обучения
true_positive = 85  # правильно предсказали "да"
false_positive = 15  # неправильно предсказали "да"
true_negative = 120  # правильно предсказали "нет"
false_negative = 10  # неправильно предсказали "нет"

# ТВОЯ ЗАДАЧА: Посчитай метрики используя операторы

# 1. Accuracy (точность) = (TP + TN) / (TP + FP + TN + FN)
accuracy = (true_positive + true_negative) / (
    true_positive + false_positive + true_negative + false_negative
)

# 2. Precision (точность положительных) = TP / (TP + FP)
precision = true_positive / (true_positive + false_positive)

# 3. Recall (полнота) = TP / (TP + FN)
recall = true_positive / (true_positive + false_negative)

# 4. F1-score = 2 * (Precision * Recall) / (Precision + Recall)
f1_score = 2 * (precision * recall) / (precision + recall)

# Выведи результаты с 2 знаками после запятой
print(f"Accuracy: {accuracy:.2f}")
print(f"Precision: {precision:.2f}")
print(f"Recall: {recall:.2f}")
print(f"F1-Score: {f1_score:.2f}")

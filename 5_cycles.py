# В ML данные обрабатываются батчами
# Представь: батч с accuracy разных моделей
batch_accuracies = [0.45, 0.89, 0.72, 0.95, 0.60, 0.91, 0.83, 0.96]

# ТВОЯ ЗАДАЧА:
# 1. Пройди циклом for по всем accuracy
# 2. Если accuracy < 0.70 — пропусти (continue)
# 3. Если accuracy >= 0.95 — выведи "Найдена топ модель!" и останови цикл (break)
# 4. Для остальных — выведи "Модель с accuracy: X.XX прошла фильтр"

# Твой код здесь:


for accuracy in batch_accuracies:
    if accuracy < 0.70:
        continue
    elif accuracy >= 0.95:
        print(f'Найдена топ модель! Ее accuracy: {accuracy}')
        break
    else:
        print(f'Модель с accuracy: {accuracy} прошла фильтр')

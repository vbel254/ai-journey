# 1. Создай кортеж с размерами нейросети (input=784, hidden=128, output=10)
network_shape = (784, 128, 10)

# 2. Выведи размер входного слоя (первый элемент)
print(f"Input layer: {network_shape[0]}")

# 3. Выведи размер выходного слоя (последний элемент)
print(f"Output layer: {network_shape[-1]}")

# 4. Попробуй изменить hidden=256 (должно вылететь с ошибкой — это нормально!)
# network_shape[1] = 256  # раскомментируй и запусти

# ЗАДАЧА 2: Распаковка кортежей
# Координаты точки в 3D пространстве
point = (10, 20, 30)

# Распакуй кортеж в переменные x, y, z
x, y, z = point

print(f"x={x}, y={y}, z={z}")

# Функция возвращает loss и accuracy
def train_model():
    return (0.35, 0.92)  # (loss, accuracy)

# Распакуй результат функции
loss, accuracy = train_model()

print(f"Loss: {loss}, Accuracy: {accuracy}")

# ЗАДАЧА 3: Кортеж с * (звёздочка) — продвинутое!
# Результаты обучения: epoch, loss1, loss2, loss3, loss4, accuracy
results = (5, 0.8, 0.6, 0.5, 0.4, 0.95)

# Распакуй: epoch в переменную, все losses в список, accuracy отдельно
epoch, *losses, accuracy = results

print(f"Epoch: {epoch}")
print(f"Losses: {losses}")
print(f"Final accuracy: {accuracy}")

# Твоя задача: распакуй этот кортеж
model_info = ("GPT-4", 2024, "OpenAI", "transformer", "LLM")
# Достань: name, year, остальное в список other_info
# твой код здесь

name, year, *other_info = model_info

print(f"Model: {name}, Year: {year}, Info: {other_info}")

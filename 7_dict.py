# # 1. Создай словарь с информацией о модели ML:
# model_config = {
#     "model_name": "GPT-4",
#     "parameters": 1800000000000,
#     "temperature": 0.7,
#     "max_tokens": 4096,
# }

# # 2. Выведи название модели

# print(model_config['model_name'])

# # 3. Выведи количество параметров

# print(model_config['parameters'])

# # 4. Попробуй получить несуществующий ключ "version" через .get()
# # (это безопаснее чем model_config["version"])

# print(model_config.get('version'))

# # 5. Добавь новый ключ "provider" со значением "OpenAI"

# model_config['provider'] = 'OpenAI'

# # 6. Измени temperature на 0.5

# model_config['temperature'] = 0.5

# # 7. Выведи весь словарь

# for key, value in model_config.items():
#     print(f'{key}: {value}')

# # ЗАДАЧА 2: Практика методов словаря
# # Данные о результатах эксперимента ML модели
# experiment = {
#     "accuracy": 0.94,
#     "precision": 0.91,
#     "recall": 0.89,
#     "f1_score": 0.90,
# }

# # 1. Получи accuracy безопасным способом (.get)

# print(experiment.get('accuracy'))

# # 2. Попробуй получить "auc" через .get с дефолтным значением 0.0

# print(experiment.get('auc', 0.0))

# # 3. Добавь новую метрику "loss": 0.15

# experiment['loss'] = 0.15

# # 4. Выведи все КЛЮЧИ словаря (используй .keys())

# print(experiment.keys())

# # 5. Выведи все ЗНАЧЕНИЯ метрик (используй .values())

# print(experiment.values())

# # 6. Найди среднее значение всех метрик
# #    (сумма значений / количество метрик)
# #    Подсказка: используй .values() и функции sum() и len()

# print(sum(experiment.values()) / len(experiment.values()))


# ФИНАЛЬНАЯ ЗАДАЧА: Вложенные словари (как в JSON!)
# Результаты нескольких моделей
models_comparison = {
    "gpt4": {
        "accuracy": 0.95,
        "speed_ms": 1200,
        "cost_per_1k": 0.03
    },
    "claude": {
        "accuracy": 0.93,
        "speed_ms": 800,
        "cost_per_1k": 0.02
    },
    "llama": {
        "accuracy": 0.89,
        "speed_ms": 400,
        "cost_per_1k": 0.001
    }
}

# 1. Выведи accuracy модели GPT-4

print(models_comparison["gpt4"]['accuracy'])

# 2. Выведи скорость (speed_ms) модели Claude

print(models_comparison["claude"]['speed_ms'])

# 3. Добавь новую модель "gemini" с параметрами:
#    accuracy: 0.94, speed_ms: 900, cost_per_1k: 0.025

models_comparison['gemini'] = {'accuracy': 0.94, 'speed_ms': 900, 'cost_per_1k': 0.025}
print(models_comparison)

# 4. Найди и выведи название самой БЫСТРОЙ модели (минимальный speed_ms)
#    Подсказка: используй цикл по .items() и переменную для хранения минимума

min_speed = float('inf')  # Бесконечность (любое число будет меньше)
fastest_model = ""        # Пустая строка для названия

for models, params in models_comparison.items():
    current_speed = params["speed_ms"]
    if current_speed < min_speed:
        min_speed = current_speed
        fastest_model = models
print(fastest_model)
# # Вместо всего цикла:
# fastest_model = min(models_comparison, key=lambda x: models_comparison[x]["speed_ms"])
# print(fastest_model)  # llama

# 5. Выведи общую стоимость 10000 токенов для ВСЕХ моделей
#    (сумма всех cost_per_1k * 10)

all_cost_per_1k = 0

for models, params in models_comparison.items():
    all_cost_per_1k += params["cost_per_1k"]

print(all_cost_per_1k * 10)
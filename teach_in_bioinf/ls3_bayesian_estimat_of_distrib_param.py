# Одноклеточное секвенирование. Данные для определения гена: 
#     1) риды: {6, 0, 15}
#     2) prior = Y (гамма)
#     3) k = 2 (варьировать)
#     4) θ = 3 (варьировать)
# Найти: 
#     1) posterior
#     2) MAP 
#     3) E
# Литература: Дурбин Эдди Крог Митчесон - "Анализ биологических последовательностей. Вероятностные модели белков и нуклеиновых к-т"

from scipy.stats import gamma

# Заданные данные
reads = [6, 0, 15]
prior_k = 2
prior_theta = 3

# Вычисление постериорного распределения
prior = gamma(prior_k, scale=prior_theta)  # Априорное распределение
likelihood = gamma(sum(reads) + prior_k, scale=1/(len(reads) + prior_theta))  # Правдоподобие
evidence = likelihood.pdf(reads).prod()  # Доказательство (правдоподобие данных)
posterior = gamma(prior_k + sum(reads), scale=1/(len(reads) + prior_theta))  # Постериорное распределение

# Нахождение MAP
values = posterior.rvs(10)  # Генерация случайных значений из постериорного распределения
MAP = values.argmax()

# Нахождение E (Expected value)
E = values.mean()

print("Постериорное распределение:", posterior.rvs(10000))
print("MAP:", values[MAP])
print("E:", E)
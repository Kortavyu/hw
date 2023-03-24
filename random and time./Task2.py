"""
В каждом заплыве участвуют два случайных спортсмена из разных сборных. Напиши программу для печати номеров спортсменов.

1) Программа должна запрашивать количество спортсменов в каждой сборной с сообщением: «Число участников сборной _:».
2) Затем должна печататься пара случайных спортсменов из разных сборных для заплыва в формате: «Пловец _ - пловец _».
"""
import random

# Запрашиваем количество спортсменов в каждой сборной
num_team1 = int(input("Число участников сборной 1: "))
num_team2 = int(input("Число участников сборной 2: "))

# Получаем список номеров спортсменов в каждой сборной
team1 = list(range(1, num_team1+1))
team2 = list(range(1, num_team2+1))

# Выбираем случайных спортсменов для плавания
swimmer1 = random.choice(team1)
swimmer2 = random.choice(team2)

# Печатаем пару спортсменов для заплыва
print(f"Пловец {swimmer1} - пловец {swimmer2}")
"""Игра угадай число"""

import numpy as np

min_number = 1
max_number = 101
number = np.random.randint(min_number, max_number)  # загадываем число


def score_game(number) -> int:
    # счетчик количество попыток
    count = 0

    # инициализация временных переменных а основе заданных пределов
    temp = max_number // 2
    predict_number = max_number // 2

    while True:
        last_predict_number = temp
        count += 1

        if predict_number > number:  # угадываемое число меньше
            if count == 1:
                last_predict_number = min_number
            temp = predict_number
            # берем половину между ранее взятым числом и текущим предпологаемым числом
            difference = abs(predict_number - last_predict_number) // 2
            if difference == 0:
                difference = 1  # корректировка, если разница равна 0
            predict_number = predict_number - difference

        elif predict_number < number:  # угадываемое число больше
            if count == 1:
                last_predict_number = max_number
            temp = predict_number
            # добавляем к текущему предпологаемому числу половину
            # между ранее взятым числом и текущим предпологаемым числом
            difference = abs(predict_number - last_predict_number) // 2
            if difference == 0:
                difference = 1  # корректировка, если разница равна 0
            predict_number = predict_number + difference

        else:
            print(f"Вы угадали число! Это число = {number}, за {count} попыток")
            break  # конец игры выход из цикла
    return count


# RUN
list_attempts = []
for j in range(1, 1000):
    list_attempts.append(score_game(number))

print("Среднее число попыток: {}".format(int(round(sum(list_attempts) / len(list_attempts), 0))))

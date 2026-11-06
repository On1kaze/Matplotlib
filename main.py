"""
Главный скрипт для запуска всех 5 заданий по Matplotlib.
Выполняет построение графиков, сохраняет их в директорию images/
и выводит ответы на аналитические вопросы.
"""

import os
from task1_line_plot import run_task1
from task2_bar_chart import run_task2
from task3_pie_chart import run_task3
from task4_histogram import run_task4
from task5_scatter_plot import run_task5


def main():
    print("=" * 60)
    print(" Практическая работа по визуализации данных в Matplotlib")
    print("=" * 60)

    os.makedirs("images", exist_ok=True)

    print("\n--- Задание 1. Построение линейного графика ---")
    run_task1(save_path="images/task1_line_plot.png", show=False)

    print("\n--- Задание 2. Сравнение успеваемости ---")
    best_subj, max_g = run_task2(save_path="images/task2_bar_chart.png", show=False)

    print("\n--- Задание 3. Анализ структуры расходов ---")
    max_cat, max_exp, share = run_task3(save_path="images/task3_pie_chart.png", show=False)

    print("\n--- Задание 4. Исследование результатов тестирования ---")
    freq_range, count = run_task4(save_path="images/task4_histogram.png", show=False)

    print("\n--- Задание 5. Исследование связи между показателями ---")
    answers_q = run_task5(save_path="images/task5_scatter_plot.png", show=False)

    print("\n" + "=" * 60)
    print(" Все графики успешно сгенерированы и сохранены в папку 'images/'!")
    print("=" * 60)


if __name__ == "__main__":
    main()

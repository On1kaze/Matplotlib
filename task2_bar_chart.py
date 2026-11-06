"""
Задание 2. Сравнение успеваемости
Даны средние оценки студентов по дисциплинам:
subjects = ['Математика', 'Физика', 'Информатика', 'Английский язык']
grades = [4.1, 3.8, 4.7, 4.3]

Постройте столбчатую диаграмму. Используйте разные цвета для столбцов,
добавьте заголовок и подпись вертикальной оси.
Определите, по какому предмету средняя оценка самая высокая.
"""

import os
import matplotlib.pyplot as plt


def run_task2(save_path="images/task2_bar_chart.png", show=False):
    subjects = ['Математика', 'Физика', 'Информатика', 'Английский язык']
    grades = [4.1, 3.8, 4.7, 4.3]

    # Разные гармоничные цвета для столбцов
    colors = ['#3498db', '#e74c3c', '#2ecc71', '#9b59b6']

    plt.figure(figsize=(9, 5.5))
    bars = plt.bar(subjects, grades, color=colors, width=0.55, edgecolor='black', linewidth=0.8)

    # Добавляем подписи значений над столбцами
    for bar in bars:
        height = bar.get_height()
        plt.annotate(
            f"{height:.1f}",
            xy=(bar.get_x() + bar.get_width() / 2, height),
            xytext=(0, 6),
            textcoords="offset points",
            ha='center',
            va='bottom',
            fontsize=11,
            fontweight='bold'
        )

    plt.title('Средняя успеваемость студентов по дисциплинам', fontsize=14, fontweight='bold', pad=15)
    plt.xlabel('Дисциплина', fontsize=12)
    plt.ylabel('Средняя оценка', fontsize=12)
    plt.ylim(0, 5.2)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()

    # Определение дисциплины с самой высокой средней оценкой
    max_grade = max(grades)
    best_subject = subjects[grades.index(max_grade)]

    print("[Задание 2] Результат анализа:")
    print(f"  Самая высокая средняя оценка ({max_grade}) по дисциплине: «{best_subject}».")

    if save_path:
        os.makedirs(os.path.dirname(save_path), exist_ok=True)
        plt.savefig(save_path, dpi=300)
        print(f"[Задание 2] График сохранён в: {save_path}")

    if show:
        plt.show()
    plt.close()

    return best_subject, max_grade


if __name__ == '__main__':
    run_task2(show=True)

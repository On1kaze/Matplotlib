"""
Задание 4. Исследование результатов тестирования
Даны результаты тестирования студентов:
results = [45, 52, 55, 58, 60, 62, 65, 67, 70, 70,
           72, 74, 75, 78, 80, 82, 85, 88, 90, 95]

Постройте гистограмму распределения результатов:
- количество интервалов — 5;
- цвет столбцов — оранжевый;
- цвет границ — чёрный;
- горизонтальная ось — «Количество баллов»;
- вертикальная ось — «Количество студентов».
Сделайте вывод: в каком диапазоне находится большинство результатов?
"""

import os
import numpy as np
import matplotlib.pyplot as plt


def run_task4(save_path="images/task4_histogram.png", show=False):
    results = [45, 52, 55, 58, 60, 62, 65, 67, 70, 70,
               72, 74, 75, 78, 80, 82, 85, 88, 90, 95]

    plt.figure(figsize=(9, 5.5))
    counts, bins, patches = plt.hist(
        results,
        bins=5,
        color='orange',
        edgecolor='black',
        linewidth=1.2,
        rwidth=0.95
    )

    # Подписи значений над интервалами
    for count, patch in zip(counts, patches):
        if count > 0:
            plt.annotate(
                f"{int(count)} студ.",
                xy=(patch.get_x() + patch.get_width() / 2, count),
                xytext=(0, 6),
                textcoords="offset points",
                ha='center',
                va='bottom',
                fontsize=11,
                fontweight='bold'
            )

    plt.title('Распределение результатов тестирования студентов', fontsize=14, fontweight='bold', pad=15)
    plt.xlabel('Количество баллов', fontsize=12)
    plt.ylabel('Количество студентов', fontsize=12)
    plt.xticks(bins)
    plt.ylim(0, max(counts) + 1.5)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()

    # Анализ интервалов
    max_idx = int(np.argmax(counts))
    most_frequent_range = f"[{bins[max_idx]:.0f} - {bins[max_idx + 1]:.0f}]"
    max_count = int(counts[max_idx])

    print("[Задание 4] Распределение по интервалам:")
    for i in range(len(counts)):
        print(f"  Интервал [{bins[i]:.0f} - {bins[i+1]:.0f}]: {int(counts[i])} студентов")
    print(f"  Вывод: большинство результатов ({max_count} студентов) находится в диапазоне {most_frequent_range} баллов.")

    if save_path:
        os.makedirs(os.path.dirname(save_path), exist_ok=True)
        plt.savefig(save_path, dpi=300)
        print(f"[Задание 4] График сохранён в: {save_path}")

    if show:
        plt.show()
    plt.close()

    return most_frequent_range, max_count


if __name__ == '__main__':
    run_task4(show=True)

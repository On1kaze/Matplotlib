"""
Задание 1. Построение линейного графика
Даны значения температуры воздуха за семь дней:
days = [1, 2, 3, 4, 5, 6, 7]
temperature = [12, 15, 14, 17, 19, 18, 21]

Необходимо:
- Построить линейный график.
- Добавить маркеры точек.
- Установить синий цвет линии.
- Добавить название графика «Температура воздуха за неделю».
- Подписать оси: «День» и «Температура, °C».
- Включить сетку.
"""

import os
import matplotlib.pyplot as plt


def run_task1(save_path="images/task1_line_plot.png", show=False):
    days = [1, 2, 3, 4, 5, 6, 7]
    temperature = [12, 15, 14, 17, 19, 18, 21]

    plt.figure(figsize=(9, 5))
    plt.plot(
        days,
        temperature,
        color="blue",
        marker="o",
        markersize=7,
        linewidth=2,
        label="Температура"
    )

    # Добавляем числовые значения над каждой точкой для наглядности
    for d, t in zip(days, temperature):
        plt.annotate(
            f"{t}°C",
            (d, t),
            textcoords="offset points",
            xytext=(0, 10),
            ha="center",
            fontsize=10,
            fontweight="bold",
            color="#1a365d"
        )

    plt.title("Температура воздуха за неделю", fontsize=14, fontweight="bold", pad=15)
    plt.xlabel("День", fontsize=12)
    plt.ylabel("Температура, °C", fontsize=12)
    plt.xticks(days)
    plt.ylim(10, 23)
    plt.grid(True, linestyle="--", alpha=0.7)
    plt.legend(loc="upper left")
    plt.tight_layout()

    if save_path:
        os.makedirs(os.path.dirname(save_path), exist_ok=True)
        plt.savefig(save_path, dpi=300)
        print(f"[Задание 1] График сохранён в: {save_path}")

    if show:
        plt.show()
    plt.close()


if __name__ == "__main__":
    run_task1(show=True)

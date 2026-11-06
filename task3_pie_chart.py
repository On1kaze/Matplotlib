"""
Задание 3. Анализ структуры расходов
Ежемесячные расходы семьи распределены следующим образом:
categories = ['Продукты', 'Транспорт', 'Коммунальные услуги', 'Связь', 'Прочее']
expenses = [120000, 30000, 45000, 15000, 40000]

Необходимо:
- Построить круговую диаграмму.
- Отобразить названия категорий.
- Вывести процент каждой категории с помощью параметра autopct.
- Добавить заголовок.
- Определить, какая категория занимает наибольшую долю расходов.
"""

import os
import matplotlib.pyplot as plt


def run_task3(save_path="images/task3_pie_chart.png", show=False):
    categories = ['Продукты', 'Транспорт', 'Коммунальные услуги', 'Связь', 'Прочее']
    expenses = [120000, 30000, 45000, 15000, 40000]

    total_expense = sum(expenses)
    max_expense = max(expenses)
    max_idx = expenses.index(max_expense)
    max_category = categories[max_idx]
    max_share = (max_expense / total_expense) * 100

    # Визуальное выделение наибольшей доли (смещение кусочка)
    explode = [0.08 if i == max_idx else 0 for i in range(len(categories))]
    colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0']

    plt.figure(figsize=(8, 7))
    plt.pie(
        expenses,
        labels=categories,
        autopct='%1.1f%%',
        startangle=140,
        explode=explode,
        colors=colors,
        shadow=True,
        textprops={'fontsize': 11}
    )

    plt.title('Анализ структуры ежемесячных расходов семьи', fontsize=14, fontweight='bold', pad=20)
    plt.tight_layout()

    print("[Задание 3] Результат анализа:")
    formatted_total = f"{total_expense:,}".replace(',', ' ')
    formatted_max = f"{max_expense:,}".replace(',', ' ')
    print(f"  Общая сумма расходов: {formatted_total} руб.")
    print(f"  Наибольшую долю расходов занимает категория «{max_category}»: {formatted_max} руб. ({max_share:.1f}%).")

    if save_path:
        os.makedirs(os.path.dirname(save_path), exist_ok=True)
        plt.savefig(save_path, dpi=300)
        print(f"[Задание 3] График сохранён в: {save_path}")

    if show:
        plt.show()
    plt.close()

    return max_category, max_expense, max_share


if __name__ == '__main__':
    run_task3(show=True)

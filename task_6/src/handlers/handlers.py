import timeit
from typing import Callable
from task_6.src.constants import food_items


def calculate_menu_stats(menu: dict[str, int]) -> tuple[int, int]:
    """Обчислює загальну кількість калорій та вартість меню."""
    total_calories = 0
    total_cost = 0

    for item, quantity in menu.items():
        total_calories += food_items[item]["calories"] * quantity
        total_cost += food_items[item]["cost"] * quantity

    return total_calories, total_cost


def get_menu_results(menu: dict[str, int], budget: int, algorithm_name: str) -> str:
    """Форматує результати меню у вигляді рядка."""
    menu_lines = (
        f"Розрахунок меню для бюджету {budget} грн за допомогою {algorithm_name}:\n"
    )
    for menu_item, quantity in menu.items():
        menu_lines += f"- {menu_item}: {quantity}\n"

    total_calories, total_cost = calculate_menu_stats(menu)

    menu_lines += f"Загальна кількість калорій: {total_calories} ккал\n"
    menu_lines += f"Загальна вартість: {total_cost} грн\n"
    menu_lines += f"Решта: {budget - total_cost} грн"
    return menu_lines


def execute_and_measure_time(
    algorithm_func: Callable, budget: int, algorithm_name: str
) -> None:
    """Виконує алгоритм та вимірює час його виконання."""
    # Виконання функції для виведення результатів
    print(get_menu_results(algorithm_func(budget), budget, algorithm_name))

    # Вимірювання часу виконання функції
    measured_func = timeit.timeit(
        stmt=lambda: get_menu_results(algorithm_func(budget), budget, algorithm_name),
        number=1,
    )
    print(f"Час виконання: {measured_func} сек\n")

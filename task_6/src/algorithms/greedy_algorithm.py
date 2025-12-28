from task_6.src.constants import food_items


def greedy_algorithm(budget: int) -> dict[str, int]:
    """Визначає меню, яке максимізує кількість калорій за заданий бюджет,
    використовуючи жадібний алгоритм. Для кожного продукту обчислюється
    співвідношення калорій до вартості, і продукти вибираються
    у порядку спадання цього співвідношення, доки бюджет не буде вичерпано."""
    food_values = [
        (food[0], food[1]["calories"] / food[1]["cost"]) for food in food_items.items()
    ]

    sorted_food_values = sorted(
        food_values, key=lambda food_value: food_value[1], reverse=True
    )

    final_menu: dict[str, int] = {}

    for food_name, _ in sorted_food_values:
        food_cost = food_items[food_name]["cost"]

        while budget >= food_cost:
            final_menu[food_name] = final_menu.get(food_name, 0) + 1
            budget -= food_cost

    return final_menu

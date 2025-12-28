from task_6.src.constants import food_items


def dynamic_programming(budget: int) -> dict[str, int]:
    """Визначає меню, яке максимізує кількість калорій за заданий бюджет,
    використовуючи динамічне програмування. Створюється таблиця,
    де для кожного можливого бюджету зберігається максимальна кількість
    калорій, яку можна отримати, а також вибрані продукти для досягнення цієї кількості."""
    results = {i: 0 for i in range(budget + 1)}
    food_choices: dict[int, str] = {}

    for current_budget in range(budget + 1):
        if current_budget == 0:
            results[current_budget] = 0
            continue

        for item, details in food_items.items():
            item_cost = details["cost"]
            item_calories = details["calories"]

            if current_budget < item_cost:
                continue

            current_budget_result = results[current_budget - item_cost] + item_calories

            if current_budget_result > results[current_budget]:
                results[current_budget] = current_budget_result
                food_choices[current_budget] = item

    menu: dict[str, int] = {}
    remaining_budget = budget
    while remaining_budget > 0:
        current_item = food_choices.get(remaining_budget)

        # Оскільки не всі бюджети можуть бути досягнуті і покупцю буде повертатись решта,
        # перевіряємо чи існує вибраний продукт для поточного бюджету. Якщо ні, зменшуємо бюджет
        # на 1 поки не знайдемо продукт або бюджет не стане 0.
        if current_item is None:
            remaining_budget -= 1
            continue

        if current_item not in menu:
            menu[current_item] = 1
        else:
            menu[current_item] += 1

        remaining_budget -= food_items[current_item]["cost"]

    return menu

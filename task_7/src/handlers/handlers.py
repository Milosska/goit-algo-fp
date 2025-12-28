import matplotlib.pyplot as plt


def show_probability_comparison_table(
    analytical_probs: dict[int, float], monte_carlo_probs: dict[int, float]
) -> str:
    table = "\nПорівняльна таблиця ймовірностей, отриманих аналітичним методом та методом Монте-Карло:"
    table += "\n------------------------------------------------------------"
    table += "\nСума очок | Аналітична ймовірність | Ймовірність Монте-Карло"
    table += "\n------------------------------------------------------------"

    for total in range(2, 13):
        analytical_prob = analytical_probs[total]
        monte_carlo_prob = monte_carlo_probs[total]
        table += f"\n {total:<9}| {analytical_prob:<23.2%}| {monte_carlo_prob:.2%}"

    table += "\n------------------------------------------------------------ \n"
    return table


def show_probability_comparison_graph(
    analytical_probs: dict[int, float], monte_carlo_probs: dict[int, float]
):
    sums = list(monte_carlo_probs.keys())
    monte_carlo_probs_values = list(monte_carlo_probs.values())
    analytical_probs_values = list(analytical_probs.values())

    plt.figure(figsize=(10, 5))
    width = 0.35

    plt.bar(
        [x - width / 2 for x in sums],
        monte_carlo_probs_values,
        width,
        color="skyblue",
        label="Ймовірність Монте-Карло",
    )
    plt.bar(
        [x + width / 2 for x in sums],
        analytical_probs_values,
        width,
        color="orange",
        alpha=0.7,
        label="Аналітична ймовірність",
    )
    plt.xticks(sums)
    plt.grid(axis="y", alpha=0.3)

    plt.xlabel("Сума двох кубиків")
    plt.ylabel("Ймовірність")
    plt.title(
        "Графік порівняння ймовірностей отриманих аналітичним методом та методом Монте-Карло"
    )
    plt.legend()

    print(
        "Графік порівняння ймовірностей відображено. Для продовження роботи закрийте вікно графіка."
    )
    plt.show()

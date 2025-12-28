from common.src import handle_errors
from task_7.src.constants import analytic_probabilities
from task_7.src.algorithms import monte_carlo_simulation
from task_7.src.handlers import (
    show_probability_comparison_table,
    show_probability_comparison_graph,
)


@handle_errors
def main():
    print(
        "Рахуємо ймовірності випадення суми очок на двох кубиках за допомогою методу Монте-Карло..."
    )
    simulation_results = monte_carlo_simulation(100000)

    print(show_probability_comparison_table(analytic_probabilities, simulation_results))

    print("Візуалізуємо отримані результати...")
    show_probability_comparison_graph(analytic_probabilities, simulation_results)

    print("Порівняння ймовірностей завершено.")


if __name__ == "__main__":
    main()

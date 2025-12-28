from common.src import handle_errors
from task_6.src.algorithms import greedy_algorithm, dynamic_programming
from task_6.src.handlers import execute_and_measure_time


@handle_errors
def main():
    print("Виконуємо порівняння алгоритмів для задачі формування меню за бюджетом...\n")

    amounts_to_compare = [126, 1055, 15294]

    for amount in amounts_to_compare:
        execute_and_measure_time(greedy_algorithm, amount, "Greedy Algorithm")
        execute_and_measure_time(dynamic_programming, amount, "Dynamic Programming")

    print("Порівняння завершено.")


if __name__ == "__main__":
    main()

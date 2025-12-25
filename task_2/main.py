from common.src import handle_errors
from task_2.src.handlers import parse_rec_depth, draw_pythagoras_tree


@handle_errors
def main():
    rec_depth = parse_rec_depth(
        input("Привіт! Введіть рівень рекурсії для побудови дерева Піфагора: ")
    )
    print(f"Рівень рекурсії встановлено на {rec_depth} рівнів.")

    print("Починаємо малювати дерево Піфагора...")
    draw_pythagoras_tree(rec_depth)
    print("Програму завершено.")


if __name__ == "__main__":
    main()

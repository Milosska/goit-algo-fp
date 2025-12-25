import turtle
from task_2.src.exceptions import DepthValueIsNotValidException


def parse_rec_depth(input_str: str) -> int:
    if not input_str.isdigit():
        raise DepthValueIsNotValidException()

    int_value = int(input_str)

    if 1 > int_value > 1000:
        raise DepthValueIsNotValidException()

    return int(input_str)


def draw_pythagoras_branch(depth: int, length: float):
    """
    Рекурсивно малює одну гілку дерева Піфагора.
    """
    if depth == 0:
        turtle.forward(length)
        turtle.backward(length)
        return

    turtle.forward(length)

    turtle.left(45)
    draw_pythagoras_branch(depth - 1, length * 0.7)
    turtle.right(45)

    turtle.right(45)
    draw_pythagoras_branch(depth - 1, length * 0.7)
    turtle.left(45)

    turtle.backward(length)


def draw_pythagoras_tree(rec_depth: int):
    """
    Налаштовує черепашку і малює дерево Піфагора заданої глибини.
    """
    turtle.speed(0)

    turtle.penup()
    turtle.goto(-50, -200)
    turtle.pendown()

    turtle.left(90)
    draw_pythagoras_branch(rec_depth, 200)

    print("Малюнок завершено. Закрийте вікно малюнка, щоб вийти з програми.")
    turtle.done()

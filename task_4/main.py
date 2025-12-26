from common.src import handle_errors
from task_4.src.handlers import build_heap
from common.src.handlers import get_binary_tree, draw_tree


@handle_errors
def main():
    # Побудова та візуалізація бінарного дерева з базової heap
    base_heap = build_heap(is_random=False)
    base_tree_root = get_binary_tree(base_heap)
    print(
        f"Будуємо бінарне дерево з базової купи {' -> '.join(str(elem) for elem in base_heap)}:"
    )
    draw_tree(base_tree_root)

    # Побудова та візуалізація бінарного дерева з випадкової heap
    random_heap = build_heap(size=10)
    random_tree_root = get_binary_tree(random_heap)
    print(
        f"\nБудуємо бінарне дерево з випадкової купи {' -> '.join(str(elem) for elem in random_heap)}:"
    )
    draw_tree(random_tree_root)


if __name__ == "__main__":
    main()

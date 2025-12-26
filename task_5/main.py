from common.src import handle_errors, DEFAULT_HEAP_VALUES
from common.src.handlers import get_binary_tree, draw_tree
from task_5.src.algorithms import bfs_algorithm, dfs_algorithm


@handle_errors
def main():
    # Побудова та візуалізація бінарного дерева з базової heap
    base_heap = DEFAULT_HEAP_VALUES
    base_tree_root = get_binary_tree(base_heap)

    bfs_tree_root = bfs_algorithm(base_tree_root)
    print("Візуалізуємо обхід бінарного дерева в ширину...")
    draw_tree(bfs_tree_root)

    dfs_tree_root = dfs_algorithm(base_tree_root)
    print("Візуалізуємо обхід бінарного дерева в глибину...")
    draw_tree(dfs_tree_root)


if __name__ == "__main__":
    main()

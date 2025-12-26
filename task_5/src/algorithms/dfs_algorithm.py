from common.src.classes import Node
from task_5.src.handlers import color_nodes


def dfs_algorithm(binary_tree_root: Node) -> Node:
    nodes_sequence: list[Node] = []

    stack: list[Node] = []
    stack.append(binary_tree_root)

    while stack:
        current_node = stack.pop()
        nodes_sequence.append(current_node)

        if current_node.right:
            stack.append(current_node.right)

        if current_node.left:
            stack.append(current_node.left)

    color_nodes(nodes_sequence)

    return nodes_sequence[0]

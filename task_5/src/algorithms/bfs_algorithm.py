from queue import Queue
from common.src.classes import Node
from task_5.src.handlers import color_nodes


def bfs_algorithm(binary_tree_root: Node) -> Node:
    nodes_sequence = []
    nodes_sequence.append(binary_tree_root)

    queue: Queue[Node] = Queue()
    queue.put(binary_tree_root)

    while not queue.empty():
        current_node = queue.get()

        if current_node.left:
            nodes_sequence.append(current_node.left)
            queue.put(current_node.left)

        if current_node.right:
            nodes_sequence.append(current_node.right)
            queue.put(current_node.right)

    color_nodes(nodes_sequence)

    return nodes_sequence[0]

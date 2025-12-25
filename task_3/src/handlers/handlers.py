import networkx as nx
import matplotlib.pyplot as plt
from typing import Any
from task_3.src.constants import graph_title, coordinates
from task_3.src.algorithms import dijkstra_heap_algorithm


def initialize_graph() -> nx.Graph:
    graph: nx.Graph = nx.Graph()
    graph.add_nodes_from(
        [
            ("Обухів", {"weight": 1, "color": "#dd4b4b"}),
            ("Таценки", {"weight": 2, "color": "#2b6fad"}),
            ("Козин", {"weight": 2, "color": "#2b6fad"}),
            ("Нові Безрадичі", {"weight": 3}),
            ("Романків", {"weight": 3}),
            ("Підгірці", {"weight": 3}),
            ("Старі Безрадичі", {"weight": 3}),
            ("Копачів", {"weight": 3}),
            ("Григорівка", {"weight": 3}),
            ("Гусачівка", {"weight": 3}),
            ("Матяшівка", {"weight": 3}),
            ("Слобідка", {"weight": 3}),
            ("Красне Перше", {"weight": 3}),
            ("Долина", {"weight": 3}),
            ("Дерев'яна", {"weight": 3}),
            ("Трипілля", {"weight": 2, "color": "#2b6fad"}),
            ("Халеп'я", {"weight": 3}),
            ("Витачів", {"weight": 3}),
            ("Стайки", {"weight": 3}),
            ("Українка", {"weight": 2, "color": "#2b6fad"}),
            ("Плюти", {"weight": 3}),
        ]
    )

    graph.add_weighted_edges_from(
        [
            ("Обухів", "Таценки", 7.8),
            ("Таценки", "Козин", 8.6),
            ("Обухів", "Нові Безрадичі", 12.2),
            ("Нові Безрадичі", "Таценки", 11.4),
            ("Нові Безрадичі", "Романків", 11.7),
            ("Романків", "Підгірці", 2.7),
            ("Обухів", "Старі Безрадичі", 12.3),
            ("Старі Безрадичі", "Копачів", 22.0),
            ("Обухів", "Григорівка", 8.1),
            ("Григорівка", "Гусачівка", 3.0),
            ("Григорівка", "Матяшівка", 3.9),
            ("Гусачівка", "Матяшівка", 5.1),
            ("Матяшівка", "Слобідка", 4.5),
            ("Обухів", "Красне Перше", 6.5),
            ("Красне Перше", "Долина", 4.4),
            ("Дерев'яна", "Трипілля", 7.8),
            ("Обухів", "Дерев'яна", 6.8),
            ("Трипілля", "Халеп'я", 4.1),
            ("Халеп'я", "Витачів", 6.4),
            ("Халеп'я", "Стайки", 7.5),
            ("Обухів", "Українка", 9.9),
            ("Українка", "Трипілля", 7.8),
            ("Українка", "Плюти", 6.0),
        ]
    )

    return graph


def handle_graph_build(graph: nx.Graph) -> None:
    # Set main params
    pos = coordinates
    node_weights = [data["weight"] for _, data in graph.nodes(data=True)]
    node_sizes = list(
        map(lambda weight: (max(node_weights) - weight + 1) * 100, node_weights)
    )
    node_colors = [
        data["color"] if "color" in data else "#2f670b"
        for _, data in graph.nodes(data=True)
    ]

    nx.draw(graph, pos, with_labels=False, node_size=node_sizes, node_color=node_colors)

    # Move node labels below the nodes
    label_pos: dict[Any, tuple[float, float]] = {
        node: (float(x), float(y) - 0.0175) for node, (x, y) in pos.items()
    }
    nx.draw_networkx_labels(graph, label_pos, font_size=7)

    # Indicate edges weight
    nx.draw_networkx_edge_labels(
        graph,
        pos,
        edge_labels={
            (u, v): f"{data['weight']} км" for u, v, data in graph.edges(data=True)
        },
        font_size=5,
    )

    plt.title(graph_title)
    print("Граф побудовано успішно! Для продовження роботи закрийте вікно з графом.")
    plt.show()


def handle_dijkstra(graph: nx.Graph, start_vertex="Обухів"):
    print(f"\nЗапускаємо алгоритм Дейкстри для графу '{graph_title}'.")
    node_min_distances = dijkstra_heap_algorithm(graph, start_vertex)

    print(f"\nНайменші відстані від населеного пункту {start_vertex}:")
    for vertex, path_data in node_min_distances.items():
        print(
            f"{' ' * 4}{vertex}: {' --> '.join(path_data[1])}. Протяжність маршруту {path_data[0]} км"
        )

    print("\nРозрахунок відстаней завершено.")

import heapq
import networkx as nx
from typing import Dict, List, Tuple


def dijkstra_heap_algorithm(
    graph: nx.Graph, start_vertex: str
) -> Dict[str, Tuple[float, List[str]]]:
    distances: Dict[str, Tuple[float, List[str]]] = {
        vertex: (float("inf"), []) for vertex in graph
    }
    distances[start_vertex] = (0.0, [start_vertex])

    distance_heap: list[tuple[float, str]] = []
    heapq.heappush(distance_heap, (0, start_vertex))

    while distance_heap:
        current_distance, current_vertex = heapq.heappop(distance_heap)

        # Якщо відстань більша за вже знайдену, пропускаємо цей вузол
        if current_distance > distances[current_vertex][0]:
            continue

        for vertex in graph.neighbors(current_vertex):
            weight = graph[current_vertex][vertex]["weight"]
            total_distance = current_distance + weight

            if total_distance < distances[vertex][0]:
                new_path = distances[current_vertex][1] + [vertex]

                distances[vertex] = (total_distance, new_path)
                heapq.heappush(distance_heap, (total_distance, vertex))

    return distances

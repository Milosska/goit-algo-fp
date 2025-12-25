from common.src import handle_errors
from task_3.src.handlers import initialize_graph, handle_graph_build, handle_dijkstra


@handle_errors
def main():
    print("Ініціалізуємо граф Обухівської громади...")
    obuchiv_graph = initialize_graph()
    handle_graph_build(obuchiv_graph)

    handle_dijkstra(obuchiv_graph)


if __name__ == "__main__":
    main()

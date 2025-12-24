from common.src import handle_errors
from .src.handlers import create_linked_list_from_array, get_merge_sorted_lists


@handle_errors
def main():
    llist_one = create_linked_list_from_array([15, 10, 45, 5, 20, 25, 35])

    # Друк зв'язного списку
    print("Зв'язний список:")
    llist_one.print_list()

    # Реверсування зв'язного списку
    llist_one.reverse_list()
    print("Зв'язний список після реверсування:")
    llist_one.print_list()

    # Сортування зв'язного списку злиттям
    llist_one.sort()
    print("Зв'язний список після сортування злиттям:")
    llist_one.print_list()

    # Злитття двох відсортованих зв'язних списків
    llist_two = create_linked_list_from_array([30, 40, 50])
    llist_three = create_linked_list_from_array([5, 15, 25, 35, 45])

    merged_list = get_merge_sorted_lists(llist_three, llist_two)
    print("Зв'язний список після злиття двох відсортованих зв'язних списків:")
    merged_list.print_list()


if __name__ == "__main__":
    main()

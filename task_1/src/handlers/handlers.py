from task_1.src.classes import LinkedList
from task_1.src.algorithms import merge_nodes


def create_linked_list_from_array(arr: list[int]):
    llist = LinkedList()

    for item in arr:
        llist.insert_at_end(item)

    return llist


def get_merge_sorted_lists(left_list: LinkedList, right_list: LinkedList) -> LinkedList:
    merged_list = LinkedList()
    merged_list.head = merge_nodes(left_list.get_head(), right_list.get_head())
    return merged_list

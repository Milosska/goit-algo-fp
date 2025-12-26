import heapq
import random
from common.src.constants import DEFAULT_HEAP_VALUES


def build_heap(is_random=True, size=10) -> list[int]:
    """
    Повертає базову або випадкову купу (heap) у вигляді списку цілих чисел.
    """
    if not is_random:
        return DEFAULT_HEAP_VALUES.copy()

    random_heap_array = [random.randint(1, 100) for _ in range(size)]
    heapq.heapify(random_heap_array)
    return random_heap_array

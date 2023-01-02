import functools
from typing import List

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

RED, WHITE, BLUE = range(3)


def dutch_flag_partition_on(pivot_index: int, A: List[int]) -> None:
    """
    Use O(n) space to sort array
    Note that this doesn't really modify A
    """
    s, e, l = [], [], []
    p = A[pivot_index]

    for i in A:
        if i < p:
            s.append(i)

        elif i == p:
            e.append(i)
        else:
            l.append(i)

    A = s + e + l


def dutch_flag_partition_sub(pivot_index: int, A: List[int]) -> None:
    """
    O(n^2) processing time to process each element
    Make one pass from the front to move smaller elements
    Make another from the back to move larger elements
    """
    l = len(A)
    p = A[pivot_index]

    for i in range(l):
        # Note: A updates as we go
        for j in range(i+1, l):
            # for all subsequent items
            # If a smaller than p value is found
            # then move to the front
            # break onto next pass
            if A[j] < p:
                A[i], A[j] = A[j], A[i]
                break

    for i in reversed(range(l)):
        for j in reversed(range(i)):
            # for all previous items
            # if a larger than p value is found
            # then move to the end
            # break onto next pass
            if A[j] > p:
                A[i], A[j] = A[j], A[i]
                break


def dutch_flag_partition(pivot_index: int, A: List[int]) -> None:
    return


@enable_executor_hook
def dutch_flag_partition_wrapper(executor, A, pivot_idx):
    count = [0, 0, 0]
    for x in A:
        count[x] += 1
    pivot = A[pivot_idx]

    executor.run(functools.partial(dutch_flag_partition, pivot_idx, A))

    i = 0
    while i < len(A) and A[i] < pivot:
        count[A[i]] -= 1
        i += 1
    while i < len(A) and A[i] == pivot:
        count[A[i]] -= 1
        i += 1
    while i < len(A) and A[i] > pivot:
        count[A[i]] -= 1
        i += 1

    if i != len(A):
        raise TestFailure('Not partitioned after {}th element'.format(i))
    elif any(count):
        raise TestFailure('Some elements are missing from original array')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('dutch_national_flag.py',
                                       'dutch_national_flag.tsv',
                                       dutch_flag_partition_wrapper))

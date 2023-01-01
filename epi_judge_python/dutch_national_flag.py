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


def dutch_flag_partition(pivot_index: int, A: List[int]) -> None:
    # pivot_index = A.index(A[pivot_index])
    # p = A[pivot_index]

    # for i in range(len(A)):
    #     if A[i] < p and i > pivot_index:
    #         A[i], A[pivot_index] = A[pivot_index], A[i]
    #         pivot_index = i
    #     if A[i] > p and i < pivot_index:
    #         A[i], A[pivot_index] = A[pivot_index], A[i]
    #         pivot_index = i


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

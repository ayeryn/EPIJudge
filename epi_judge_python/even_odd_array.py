import collections
import functools
from typing import List

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


def even_odd_unordered(A: List[int]) -> None:
    """
    Add odd elements from the end and even elements from
    then end. This created an unordered list of seperation
    """
    s = 0
    e = len(A)
    temp = A
    e -= 1

    for a in temp:
        if a % 2:
            # odd -> add from end
            A[e] = a
            e -= 1
        else:
            A[s] = a
            s += 1


def even_odd_unordered(A: List[int]) -> None:
    return


@enable_executor_hook
def even_odd_wrapper(executor, A):
    before = collections.Counter(A)

    executor.run(functools.partial(even_odd, A))

    in_odd = False
    for a in A:
        if a % 2 == 0:
            if in_odd:
                raise TestFailure('Even elements appear in odd part')
        else:
            in_odd = True
    after = collections.Counter(A)
    if before != after:
        raise TestFailure('Elements mismatch')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('even_odd_array.py',
                                       'even_odd_array.tsv', even_odd_wrapper))

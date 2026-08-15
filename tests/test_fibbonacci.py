import pytest
import types

from src.gha_fibonacci.fibonacci import fibonacci


def test_function_exist() -> None:
    assert isinstance(fibonacci, types.FunctionType)


testdata = [
    (0, 0),
    (1, 1),
    (2, 1),
    (3, 2),
    (4, 3),
    (5, 5),
    (6, 8),
    (9, 34),
    (10, 55),
    (11, 89),
    (12, 144)
]


@pytest.mark.parametrize('n,excepted', testdata)
def test_should_fibonacci_expected_value(n: int, excepted: int) -> None:
    assert fibonacci(n) == excepted

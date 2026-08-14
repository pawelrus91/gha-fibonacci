import types

from src.gha_fibonacci.fibonacci import fibonacci


def test_function_exist() -> None:
    assert isinstance(fibonacci, types.FunctionType)

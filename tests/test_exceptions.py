import pytest
from src.solution import get_min_n_to_be_in_expr


def test_syntax_error():
    with pytest.raises(SyntaxError) as error:
        get_min_n_to_be_in_expr("abc+!*", 2, 0)
    assert str(error.value) == "invalid syntax"

    with pytest.raises(SyntaxError) as error:
        get_min_n_to_be_in_expr("ab.cb.+a", 3, 1)
    assert str(error.value) == "incorrect expression form"


def test_runtime_error():
    with pytest.raises(RuntimeError) as error:
        get_min_n_to_be_in_expr("a+abc..ac.bb**", 5, 3)
    assert str(error.value) == "not enough arguments"

    with pytest.raises(RuntimeError) as error:
        get_min_n_to_be_in_expr("a*b..ac+aa.", 6, 2)
    assert str(error.value) == "not enough arguments"

    with pytest.raises(RuntimeError) as error:
        get_min_n_to_be_in_expr("*abc+.acb++ab*", 3, 1)
    assert str(error.value) == "not enough arguments"

import pytest
from src.solution import get_min_n_to_be_in_expr


def test_basic():
    expression = "ab+c.aba.*.bac.+.+*"
    assert get_min_n_to_be_in_expr(expression, 3, 1) == 4


def test_inf():
    expression = "acb..bab.c.*.ab.ba.+.+*a."
    assert get_min_n_to_be_in_expr(expression, 3, 0) == "INF"


def test_basic_2():
    expression = "1a+b.*"
    assert get_min_n_to_be_in_expr(expression, 4, 3) == 3


def test_basic_3():
    expression = "acb..bab.c.*.ab.ba.+.+*a."
    assert get_min_n_to_be_in_expr(expression, 7, 4) == 4


def test_inf_2():
    expression = "ab.*"
    assert get_min_n_to_be_in_expr(expression, 6, 3) == "INF"

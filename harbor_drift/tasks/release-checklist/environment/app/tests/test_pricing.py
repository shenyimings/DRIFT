import pytest

from inventory.pricing import apply_discount, line_total


def test_no_discount():
    assert apply_discount(10.0, 0) == 10.0


def test_ten_percent():
    assert apply_discount(4.50, 10) == 4.05


def test_bad_percent():
    with pytest.raises(ValueError):
        apply_discount(1.0, 120)


def test_line_total():
    assert line_total(19.99, 2, 25) == 29.98

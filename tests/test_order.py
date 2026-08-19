from classes.Order import Order
from exceptions import InvalidOrderError
import pytest


def test_valid_order():
    order = Order(
        "1",
        "2026-08-19",
        "Alice",
        "Laptop",
        "Electronics",
        "2",
        "100",
    )

    assert order.order_id == 1
    assert order.quantity == 2
    assert order.price == 100


def test_invalid_id_order():
    with pytest.raises(InvalidOrderError):
        Order(
            "invalid",
            "2026-08-19",
            "Alice",
            "Laptop",
            "Electronics",
            "2",
            "100",
        )


def test_negative_id_order():
    with pytest.raises(InvalidOrderError):
        Order(
            "-1",
            "2026-08-19",
            "Alice",
            "Laptop",
            "Electronics",
            "2",
            "100",
        )


def test_no_customer_in_order():
    with pytest.raises(InvalidOrderError):
        Order(
            "32",
            "2026-08-19",
            "",
            "Laptop",
            "Electronics",
            "2",
            "100",
        )


def test_no_product_in_order():
    with pytest.raises(InvalidOrderError):
        Order(
            "32",
            "2026-08-19",
            "Saeed",
            "",
            "Electronics",
            "2",
            "100",
        )


def test_no_category_in_order():
    with pytest.raises(InvalidOrderError):
        Order(
            "32",
            "2026-08-19",
            "Saeed",
            "Laptop",
            "",
            "2",
            "100",
        )


def test_no_order_date():
    with pytest.raises(InvalidOrderError):
        Order(
            "32",
            "",
            "Saeed",
            "Laptop",
            "Electronics",
            "2",
            "100",
        )


def test_invalid_order_date():
    with pytest.raises(InvalidOrderError):
        Order(
            "32",
            "26-0998-19",
            "Saeed",
            "Laptop",
            "Electronics",
            "2",
            "100",
        )


def test_invalid_quantity():
    with pytest.raises(InvalidOrderError):
        Order(
            "1",
            "2026-08-19",
            "Alice",
            "Laptop",
            "Electronics",
            "invalid",
            "100",
        )


def test_negative_quantity():
    with pytest.raises(InvalidOrderError):
        Order(
            "1",
            "2026-08-19",
            "Alice",
            "Laptop",
            "Electronics",
            "-2",
            "100",
        )


def test_invalid_price():
    with pytest.raises(InvalidOrderError):
        Order(
            "1",
            "2026-08-19",
            "Alice",
            "Laptop",
            "Electronics",
            "3",
            "",
        )


def test_negative_price():
    with pytest.raises(InvalidOrderError):
        Order(
            "1",
            "2026-08-19",
            "Alice",
            "Laptop",
            "Electronics",
            "2",
            "-100",
        )

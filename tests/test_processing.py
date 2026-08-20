from classes.order import Order
from processing_logic import (
    get_top_products_by_revenue,
    get_top_spending_customers,
    get_revenue_per_category,
    get_total_revenue,
    get_total_orders,
)


def test_total_orders() -> None:
    orders = [
        Order(
            "1", "2026-08-19", "Alice", "Laptop", "Electronics", "2", "1000"
        ),
        Order("2", "2026-08-19", "Bob", "Phone", "Electronics", "5", "300"),
        Order("3", "2026-08-19", "Charlie", "Desk", "Furniture", "3", "400"),
    ]

    result = get_total_orders(orders)

    assert result == 3


def test_total_revenue() -> None:
    orders = [
        Order(
            "1", "2026-08-19", "Alice", "Laptop", "Electronics", "2", "1000"
        ),
        Order("2", "2026-08-19", "Bob", "Phone", "Electronics", "5", "300"),
        Order("3", "2026-08-19", "Charlie", "Desk", "Furniture", "3", "400"),
    ]

    result = get_total_revenue(orders)

    assert result == 4700


def test_top_5_products_by_revenue() -> None:
    orders = [
        Order(
            "1", "2026-08-19", "Alice", "Laptop", "Electronics", "2", "1000"
        ),
        Order("2", "2026-08-19", "Bob", "Phone", "Electronics", "5", "300"),
        Order("3", "2026-08-19", "Charlie", "Desk", "Furniture", "3", "400"),
        Order("4", "2026-08-19", "David", "Chair", "Furniture", "10", "80"),
        Order("5", "2026-08-19", "Eva", "Monitor", "Electronics", "4", "250"),
        Order(
            "6", "2026-08-19", "Frank", "Keyboard", "Electronics", "1", "50"
        ),
    ]

    result = get_top_products_by_revenue(orders)

    assert len(result) == 5
    assert result[0]["product"] == "Laptop"
    assert result[1]["product"] == "Phone"
    assert result[-1]["product"] == "Chair"


def test_top_5_customers_by_spending() -> None:
    orders = [
        Order(
            "1", "2026-08-19", "Alice", "Laptop", "Electronics", "2", "1000"
        ),
        Order("2", "2026-08-19", "Bob", "Phone", "Electronics", "5", "300"),
        Order("3", "2026-08-19", "Alice", "Desk", "Furniture", "3", "400"),
        Order("4", "2026-08-19", "Charlie", "Chair", "Furniture", "10", "80"),
        Order(
            "5", "2026-08-19", "David", "Monitor", "Electronics", "4", "250"
        ),
        Order("6", "2026-08-19", "Bob", "Keyboard", "Electronics", "1", "50"),
        Order("7", "2026-08-19", "Charlie", "Mouse", "Electronics", "5", "40"),
        Order("8", "2026-08-19", "Eva", "Printer", "Electronics", "2", "300"),
    ]

    result = get_top_spending_customers(orders)

    assert len(result) == 5
    assert result[0][0] == "Alice"
    assert result[1][0] == "Bob"
    assert result[2][0] == "Charlie"
    assert result[3][0] == "David"
    assert result[4][0] == "Eva"
    assert result[-1][0] == "Eva"


def test_revenue_per_category() -> None:
    orders = [
        Order(
            "1", "2026-08-19", "Alice", "Laptop", "Electronics", "2", "1000"
        ),
        Order("2", "2026-08-19", "Bob", "Phone", "Electronics", "5", "300"),
        Order("3", "2026-08-19", "Charlie", "Desk", "Furniture", "3", "400"),
        Order("4", "2026-08-19", "David", "Chair", "Furniture", "10", "80"),
        Order("5", "2026-08-19", "Eva", "Monitor", "Electronics", "4", "250"),
        Order("6", "2026-08-19", "Frank", "Sofa", "Furniture", "2", "600"),
        Order("7", "2026-08-19", "Grace", "Book", "Books", "10", "20"),
        Order("8", "2026-08-19", "Henry", "Novel", "Books", "5", "30"),
    ]

    result = get_revenue_per_category(orders)

    assert len(result) == 3
    assert result[0] == ("Electronics", 4500)
    assert result[1] == ("Furniture", 3200)
    assert result[2] == ("Books", 350)

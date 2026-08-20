from classes.order import Order
from classes.types import ProductRevenue


def get_total_orders(orders_list: list[Order]) -> int:
    return len(orders_list)


def get_total_revenue(orders_list: list[Order]) -> float:
    total = 0.0
    for order in orders_list:
        total += order.get_revenue()
    return total


def get_top_products_by_revenue(
    orders_list: list[Order], limit: int = 5
) -> list[ProductRevenue]:
    sorted_list_by_product_revenue = sorted(
        orders_list, key=lambda order: order.get_revenue(), reverse=True
    )

    sorted_product_with_price_list: list[ProductRevenue] = [
        {"product": order.product, "revenue": order.get_revenue()}
        for order in sorted_list_by_product_revenue
    ]

    return sorted_product_with_price_list[:limit]


def get_top_spending_customers(
    orders_list: list[Order], limit: int = 5
) -> list[tuple[str, float]]:
    customers_dict: dict[str, float] = {}

    for order in orders_list:
        customer_name = order.customer
        order_total_revenue = order.get_revenue()
        customers_dict[customer_name] = (
            customers_dict.get(customer_name, 0) + order_total_revenue
        )

    sorted_customers_list = sorted(
        customers_dict.items(), key=lambda customer: customer[1], reverse=True
    )
    return sorted_customers_list[:limit]


def get_revenue_per_category(
    orders_list: list[Order],
) -> list[tuple[str, float]]:
    categories_dict: dict[str, float] = {}

    for order in orders_list:
        category_name = order.category
        order_total_revenue = order.get_revenue()
        categories_dict[category_name] = (
            categories_dict.get(category_name, 0) + order_total_revenue
        )

    sorted_categories_list = sorted(
        categories_dict.items(), key=lambda category: category[1], reverse=True
    )
    return sorted_categories_list

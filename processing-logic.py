def get_total_orders(orders_list):
    return len(orders_list)


def get_total_revenue(orders_list):
    total = 0
    for order in orders_list:
        total += order.get_revenue()
    return total


def get_top_products_by_revenue(orders_list, limit=5):
    sorted_list_by_product_revenue = sorted(
        orders_list, key=lambda order: order.get_revenue(), reverse=True
    )

    sorted_product_with_price_list = [
        {"product": order.product, "price": order.price}
        for order in sorted_list_by_product_revenue
    ]

    return sorted_product_with_price_list[:limit]


def get_top_spending_customers(orders_list, limit=5):
    customers_dict = {}

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


def get_revenue_per_category(orders_list):
    categories_dict = {}

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

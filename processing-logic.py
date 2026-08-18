def get_total_orders(orders_list):
    total_orders = len(orders_list)
    return total_orders


def get_total_revenue(orders_list):
    total = 0
    for order_dic in orders_list:
        total += float(order_dic["price"]) * int(order_dic["quantity"])
    return total


def get_top_products_by_revenue(orders_list, limit=5):
    sorted_list_by_product_revenue = sorted(
        orders_list, key=lambda order: float(order["price"]), reverse=True
    )

    sorted_product_with_price_list = [
        {"product": order_dict["product"], "price": float(order_dict["price"])}
        for order_dict in sorted_list_by_product_revenue
    ]

    return sorted_product_with_price_list[:limit]


def get_top_spending_customers(orders_list, limit=5):
    customers_dict = {}

    for order_dict in orders_list:
        customer_name = order_dict["customer"]
        order_total_revenue = float(order_dict["price"]) * int(order_dict["quantity"])
        customers_dict[customer_name] = (
            customers_dict.get(customer_name, 0) + order_total_revenue
        )

    sorted_customers_list = sorted(
        customers_dict.items(), key=lambda customer: customer[1], reverse=True
    )
    return sorted_customers_list[:limit]


def get_revenue_per_category(orders_list):
    categories_dict = {}

    for order_dict in orders_list:
        category_name = order_dict["category"]
        order_total_revenue = float(order_dict["price"]) * int(order_dict["quantity"])
        categories_dict[category_name] = (
            categories_dict.get(category_name, 0) + order_total_revenue
        )

    sorted_categories_list = sorted(
        categories_dict.items(), key=lambda category: category[1], reverse=True
    )
    return sorted_categories_list

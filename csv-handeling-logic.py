import csv
from .classes.Order import Order


def read_csv(file_path):
    try:
        with open(file_path, newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            orders_data_list = []
            for order_row in reader:
                new_order = Order(
                    order_row["order_id"],
                    order_row["date"],
                    order_row["customer"],
                    order_row["product"],
                    order_row["category"],
                    order_row["quantity"],
                    order_row["price"],
                )
                orders_data_list.append(new_order)

        return orders_data_list
    except FileNotFoundError:
        print(f"File not found at the provided path: {file_path}")
        return None

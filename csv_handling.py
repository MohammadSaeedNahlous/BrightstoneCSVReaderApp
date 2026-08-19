import csv
from classes.Order import Order
from exceptions import (
    MissingColumnError,
    InvalidCSVRow,
    InvalidOrderError,
    InvalidCSVError,
)


def read_csv(file_path):

    with open(file_path, newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        required_columns = {
            "order_id",
            "date",
            "customer",
            "product",
            "category",
            "quantity",
            "price",
        }
        missing_columns = required_columns - set(reader.fieldnames or [])
        if missing_columns:
            raise MissingColumnError(f"Missing columns: {', '.join(missing_columns)}")
        orders_data_list = []
        for row in reader:
            if any(value is None for value in row.values()):
                raise InvalidCSVRow("CSV row contains missing values.")

            try:
                new_order = Order(
                    row["order_id"],
                    row["date"],
                    row["customer"],
                    row["product"],
                    row["category"],
                    row["quantity"],
                    row["price"],
                )
            except InvalidOrderError as error:
                raise InvalidCSVRow(f"Invalid CSV row: {error}") from error

            orders_data_list.append(new_order)
        if not orders_data_list:
            raise InvalidCSVError("CSV file is empty.")

    return orders_data_list

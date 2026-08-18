import csv


def read_csv(file_path):
    try:
        with open(file_path, newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            orders_data_list = list(reader)
        return orders_data_list
    except FileNotFoundError:
        print(f"File not found at the provided path: {file_path}")
        return None

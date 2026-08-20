import pytest
from csv_handling import read_csv
from classes.Order import Order
from exceptions import (
    InvalidCSVError,
    MissingColumnError,
    InvalidCSVRow,
    InvalidOrderError,
)


def test_valid_csv(tmp_path):

    csv_file = tmp_path / "orders.csv"

    csv_file.write_text(
        "order_id,date,customer,product,category,quantity,price\n"
        "1,2026-08-19,John,Laptop,Electronics,2,100.00\n",
        encoding="utf-8",
    )

    orders = read_csv(csv_file)

    assert orders is not None
    assert len(orders) > 0
    assert isinstance(orders[0], Order)


def test_empty_csv(tmp_path):

    csv_file = tmp_path / "orders.csv"

    csv_file.write_text(
        "order_id,date,customer,product,category,quantity,price\n",
        encoding="utf-8",
    )

    with pytest.raises(InvalidCSVError):
        read_csv(csv_file)


def test_missing_column(tmp_path):

    csv_file = tmp_path / "orders.csv"

    csv_file.write_text(
        "order_id,date,customer,product,category,\n"
        "1,2026-08-19,John,Laptop,Electronics\n",
        encoding="utf-8",
    )

    with pytest.raises(MissingColumnError):
        read_csv(csv_file)


def test_invalid_csv_row(tmp_path):
    csv_file = tmp_path / "broken.csv"

    csv_file.write_text(
        "order_id,date,customer,product,category,quantity,price\n"
        "1,not-a-date,Alice,Laptop,Electronics,2,100\n",
        encoding="utf-8",
    )

    with pytest.raises(InvalidCSVRow):
        read_csv(csv_file)


def test_broken_row_due_missing_values(tmp_path):

    csv_file = tmp_path / "orders.csv"

    csv_file.write_text(
        "order_id,date,customer,product,category,quantity,price\n"
        "1,2026-08-19,John,Laptop,Electronics\n",
        encoding="utf-8",
    )

    with pytest.raises(InvalidCSVRow):
        read_csv(csv_file)

from datetime import date

from exceptions import InvalidOrderError


class Order:
    def __init__(
        self,
        order_id: str,
        order_date: str,
        customer: str,
        product: str,
        category: str,
        quantity: str,
        price: str,
    ) -> None:

        if not customer.strip():
            raise InvalidOrderError("Customer cannot be empty.")

        if not product.strip():
            raise InvalidOrderError("Product cannot be empty.")

        if not category or not category.strip():
            raise InvalidOrderError("Category is required.")

        try:
            self.order_id = int(order_id)
        except (TypeError, ValueError):
            raise InvalidOrderError("Order ID must be an integer.")

        if self.order_id <= 0:
            raise InvalidOrderError("Order ID must be greater than 0.")

        if not order_date or not order_date.strip():
            raise InvalidOrderError("Date is required.")

        try:
            self.date = date.fromisoformat(order_date)
        except ValueError:
            raise InvalidOrderError("Date must be in YYYY-MM-DD format.")

        try:
            self.quantity = int(quantity)
        except (TypeError, ValueError):
            raise InvalidOrderError("Quantity must be an integer.")

        if self.quantity <= 0:
            raise InvalidOrderError("Quantity must be greater than 0.")

        try:
            self.price = float(price)
        except (TypeError, ValueError):
            raise InvalidOrderError("Price must be a number.")

        if self.price < 0:
            raise InvalidOrderError("Price cannot be negative.")

        self.customer = customer.strip()
        self.product = product.strip()
        self.category = category.strip()

    def get_revenue(self) -> float:
        return self.price * self.quantity

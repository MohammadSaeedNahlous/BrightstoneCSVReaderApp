from datetime import date


class Order:
    def __init__(
        self, order_id, order_date, customer, product, category, quantity, price
    ):

        if not customer.strip():
            raise ValueError("Customer cannot be empty.")

        if not product.strip():
            raise ValueError("Product cannot be empty.")

        if not category or not category.strip():
            raise ValueError("Category is required.")

        try:
            self.order_id = int(order_id)
        except (TypeError, ValueError):
            raise ValueError("Order ID must be an integer.")

        if self.order_id <= 0:
            raise ValueError("Order ID must be greater than 0.")

        if not order_date or not order_date.strip():
            raise ValueError("Date is required.")

        try:
            self.date = date.fromisoformat(order_date)
        except ValueError:
            raise ValueError("Date must be in YYYY-MM-DD format.")

        try:
            self.quantity = int(quantity)
        except (TypeError, ValueError):
            raise ValueError("Quantity must be an integer.")

        if self.quantity <= 0:
            raise ValueError("Quantity must be greater than 0.")

        try:
            self.price = float(price)
        except (TypeError, ValueError):
            raise ValueError("Price must be a number.")

        if self.price < 0:
            raise ValueError("Price cannot be negative.")

        self.customer = customer.strip()
        self.product = product.strip()
        self.category = category.strip()

    def get_revenue(self):
        return self.price * self.quantity

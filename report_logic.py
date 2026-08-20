import datetime as dt
import json
from pathlib import Path

from classes.types import ProductRevenue


def generate_json_report(
    total_number_of_orders: int,
    total_revenue: float,
    top_5_products_by_revenue: list[ProductRevenue],
    top_5_customers_by_total_spend: list[tuple[str, float]],
    revenue_by_category: list[tuple[str, float]],
    file_name: str | Path,
) -> None:
    timestamp = dt.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

    data = {
        "total_number_of_order": total_number_of_orders,
        "total_revenue": total_revenue,
        "top_5_products_by_revenue": top_5_products_by_revenue,
        "top_5_customers_by_total_spend": top_5_customers_by_total_spend,
        "revenue_by_category": revenue_by_category,
        "created_at": timestamp,
    }
    with open(file_name, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)


def initialize_markdown_report(
    total_number_of_orders: int,
    total_revenue: float,
    top_5_products_by_revenue: list[ProductRevenue],
    top_5_customers_by_total_spend: list[tuple[str, float]],
    revenue_by_category: list[tuple[str, float]],
    timestamp: str,
) -> str:
    report = f"""<h4 style="color: #274c77;text-align:center">
    Brightstone Logistics Report</h4>

**Generated:** {timestamp.replace("_", " ")}

<h5 style="color: #6096ba;">Summary</h5>

- **Total orders:** {total_number_of_orders}
- **Total revenue:** €{total_revenue:,.2f}

<h5 style="color: #6096ba;">Top 5 Products by Revenue</h5>

"""

    for product in top_5_products_by_revenue:
        report += f"- **{product['product']}** : €{product['revenue']:,.2f}\n"

    report += "\n<h5 style='color: #6096ba;'>Top 5 Spending Customers</h5>\n\n"

    for customer, spending in top_5_customers_by_total_spend:
        report += f"- **{customer}** : €{spending:,.2f}\n"

    report += "\n<h5 style='color: #6096ba;'>Revenue by Category</h5>\n\n"

    for category, revenue in revenue_by_category:
        report += f"- **{category}** : €{revenue:,.2f}\n"

    report += (
        "\n\n## <h6 style='color: #6096ba;'>Notes </h6>\n"
        "- Report generated automatically from the provided order data.\n"
        "- Revenue is calculated as quantity × unit price.\n"
        "- Products are ranked by revenue."
    )

    return report


def generate_markdown_report(
    total_number_of_orders: int,
    total_revenue: float,
    top_5_products_by_revenue: list[ProductRevenue],
    top_5_customers_by_total_spend: list[tuple[str, float]],
    revenue_by_category: list[tuple[str, float]],
    file_name: str | Path,
) -> None:
    timestamp = dt.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

    report = initialize_markdown_report(
        total_number_of_orders,
        total_revenue,
        top_5_products_by_revenue,
        top_5_customers_by_total_spend,
        revenue_by_category,
        timestamp,
    )

    with open(file_name, "w", encoding="utf-8") as file:
        file.write(report)

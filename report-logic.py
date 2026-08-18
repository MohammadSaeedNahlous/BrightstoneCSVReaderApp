import datetime as dt
import json
import os


def generate_json_report(
    total_number_of_order,
    total_revenue,
    top_5_products_by_revenue,
    top_5_customers_by_total_spend,
    revenue_by_category,
    output_path,
):

    data = {
        "total number of order": total_number_of_order,
        "total revenue": total_revenue,
        "top 5 products by revenue": top_5_products_by_revenue,
        "top 5 customers by total spend": top_5_customers_by_total_spend,
        "revenue by category": revenue_by_category,
    }
    try:
        timestamp = dt.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        file_name = f"report_{timestamp}.json"
        os.makedirs(output_path, exist_ok=True)
        file_path = os.path.join(output_path, file_name)
        with open(file_path, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)
    except OSError as error:
        print(f"Could not create the report: {error}")

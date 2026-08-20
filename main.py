import argparse
import logging
import sys

from processing_logic import (
    get_total_orders,
    get_total_revenue,
    get_top_products_by_revenue,
    get_top_spending_customers,
    get_revenue_per_category,
)
from report_logic import generate_json_report, generate_markdown_report
from csv_handling import read_csv
from exceptions import InvalidCSVRow, InvalidCSVError, MissingColumnError

logger = logging.getLogger(__name__)

logging.basicConfig(
    level=logging.ERROR,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

parser = argparse.ArgumentParser(
    description="Required. Generate a report from a Brightstone Logistics orders CSV file."
)
parser.add_argument("--input", required=True, help="The name of the input CSV file.")

parser.add_argument(
    "--output",
    required=True,
    help="Required. The name of the report file with the extension.",
)

parser.add_argument(
    "--format",
    choices=["markdown", "json"],
    default="markdown",
    help="Optional. The format of the generated report, either markdown(.mk) or JSON (.json). Default markdown.",
)


def main():
    arguments = parser.parse_args()
    try:
        orders = read_csv(arguments.input)

        total_number_of_orders = get_total_orders(orders)
        total_revenue = get_total_revenue(orders)
        top_5_products_by_revenue = get_top_products_by_revenue(orders)
        top_5_customers_by_total_spend = get_top_spending_customers(orders)
        revenue_by_category = get_revenue_per_category(orders)

        if arguments.format.low() == "json":
            generate_json_report(
                total_number_of_orders,
                total_revenue,
                top_5_products_by_revenue,
                top_5_customers_by_total_spend,
                revenue_by_category,
                arguments.output,
            )
        else:
            generate_markdown_report(
                total_number_of_orders,
                total_revenue,
                top_5_products_by_revenue,
                top_5_customers_by_total_spend,
                revenue_by_category,
                arguments.output,
            )
        return 0



    except InvalidCSVError as error:
        logger.error(error)
        return 1

    except InvalidCSVRow as error:
        logger.error(error)
        return 1

    except MissingColumnError as error:
        logger.error(error)
        return 1

    except FileNotFoundError as error:
        logger.error(error)
        return 1

    except OSError as error:
        logger.error(error)
        return 2


if __name__ == "__main__":
    sys.exit(main())

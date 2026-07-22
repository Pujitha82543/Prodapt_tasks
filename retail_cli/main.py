import argparse
import datetime
import logging
import sys

from calculations import check_stock_flags
from config import DEFAULT_REORDER_THRESHOLD
from io_utils import load_inventory, load_sales, write_report
from reporting import build_report, print_summary


def main():

    parser = argparse.ArgumentParser()

    parser.add_argument("--inventory", required=True)

    parser.add_argument("--sales", required=True)

    parser.add_argument("--output", required=True)

    parser.add_argument(
        "--reorder-threshold",
        type=int,
        default=DEFAULT_REORDER_THRESHOLD
    )

    args = parser.parse_args()

    logging.basicConfig(
        filename="logs/app.log",
        level=logging.INFO,
        format="%(asctime)s %(levelname)s %(message)s"
    )

    inventory = load_inventory(args.inventory)

    sales, total_rows, malformed = load_sales(args.sales)

    if total_rows > 0 and malformed / total_rows > 0.10:
        logging.critical("More than 10 percent malformed rows.")
        sys.exit(1)

    qty_sold_map = {}

    revenue_by_category = {}

    revenue_by_channel = {}

    unknown_skus = set()

    total_revenue = 0

    for sale in sales:

        if sale.sku not in inventory:
            unknown_skus.add(sale.sku)
            continue

        product = inventory[sale.sku]

        revenue = sale.line_revenue(product)

        total_revenue += revenue

        qty_sold_map[sale.sku] = qty_sold_map.get(sale.sku, 0) + sale.qty_sold

        revenue_by_category[product.category] = (
            revenue_by_category.get(product.category, 0) + revenue
        )

        revenue_by_channel[sale.channel] = (
            revenue_by_channel.get(sale.channel, 0) + revenue
        )

    revenue_by_category = {
        k: round(v, 2)
        for k, v in revenue_by_category.items()
    }

    revenue_by_channel = {
        k: round(v, 2)
        for k, v in revenue_by_channel.items()
    }

    total_revenue = round(total_revenue, 2)

    oversold, low_stock = check_stock_flags(
        inventory,
        qty_sold_map,
        args.reorder_threshold
    )

    report = build_report(
        total_revenue,
        revenue_by_category,
        revenue_by_channel,
        oversold,
        low_stock,
        unknown_skus
    )

    write_report(report, args.output)

    # print("\n------ Daily Reconciliation Report ------")
    # print("Total Revenue :", total_revenue)
    # print("Revenue by Category :", revenue_by_category)
    # print("Revenue by Channel :", revenue_by_channel)
    # print("Oversold SKUs :", oversold)
    # print("Low Stock SKUs :", low_stock)
    # print("Unknown SKUs :", unknown_skus)
    print_summary(report)


if __name__ == "__main__":

    print(f"Retail Inventory CLI - {datetime.date.today()}")

    main()
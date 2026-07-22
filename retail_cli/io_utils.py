import csv
import json
import logging

from models import Product, SaleTransaction


def parse_sale_row(row: dict):

    try:
        return SaleTransaction(
            row["sku"],
            int(row["qty_sold"]),
            float(row["discount_pct"]),
            row["channel"]
        )

    except (ValueError, KeyError):
        raise ValueError("Malformed row")


def load_inventory(json_path: str):

    inventory = {}

    with open(json_path, "r") as file:

        data = json.load(file)

        for item in data:

            inventory[item["sku"]] = Product(
                item["sku"],
                item["name"],
                item["unit_price"],
                item["stock_qty"],
                item["category"]
            )

    return inventory


def load_sales(csv_path: str):

    sales = []

    total_rows = 0
    malformed = 0

    with open(csv_path, newline="") as file:

        reader = csv.DictReader(file)

        for row in reader:

            total_rows += 1

            try:
                sales.append(parse_sale_row(row))

            except ValueError:
                malformed += 1
                logging.error(f"Malformed row skipped : {row}")

    return sales, total_rows, malformed


def write_report(report: dict, output_path: str):

    with open(output_path, "w") as file:

        json.dump(report, file, indent=4)
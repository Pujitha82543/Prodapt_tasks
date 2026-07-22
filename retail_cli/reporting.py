def build_report(
    total_revenue,
    revenue_by_category,
    revenue_by_channel,
    oversold,
    low_stock,
    unknown_skus
):
    return {
        "Total Revenue": total_revenue,
        "Revenue by Category": revenue_by_category,
        "Revenue by Channel": revenue_by_channel,
        "Oversold SKUs": list(oversold),
        "Low Stock SKUs": list(low_stock),
        "Unknown SKUs": list(unknown_skus)
    }


def print_summary(report):
    print("\n------ Daily Reconciliation Report ------")

    print(f"Total Revenue : {report['Total Revenue']}")

    print("\nRevenue by Category:")
    for category, revenue in report["Revenue by Category"].items():
        print(f"  {category}: {revenue}")

    print("\nRevenue by Channel:")
    for channel, revenue in report["Revenue by Channel"].items():
        print(f"  {channel}: {revenue}")

    print("\nOversold SKUs:")
    if report["Oversold SKUs"]:
        for sku in report["Oversold SKUs"]:
            print(f"  {sku}")
    else:
        print("  None")

    print("\nLow Stock SKUs:")
    if report["Low Stock SKUs"]:
        for sku in report["Low Stock SKUs"]:
            print(f"  {sku}")
    else:
        print("  None")

    print("\nUnknown SKUs:")
    if report["Unknown SKUs"]:
        for sku in report["Unknown SKUs"]:
            print(f"  {sku}")
    else:
        print("  None")
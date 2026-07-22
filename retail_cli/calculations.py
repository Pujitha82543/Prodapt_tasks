def compute_revenue(unit_price, qty_sold, discount_pct):
    if discount_pct < 0:
        discount_pct = 0
    elif discount_pct > 100:
        discount_pct = 100

    revenue = qty_sold * unit_price * (1 - discount_pct / 100)

    return round(revenue, 2)


def category_code_from_sku(sku: str):
    return sku[4:7]


def check_stock_flags(inventory, qty_sold_map, reorder_threshold):
    oversold = set()
    low_stock = set()

    for sku, product in inventory.items():

        sold = qty_sold_map.get(sku, 0)

        if sold > product.stock_qty:
            oversold.add(sku)

        if product.remaining_stock(sold) < reorder_threshold:
            low_stock.add(sku)

    return oversold, low_stock
from calculations import compute_revenue


class Product:
    def __init__(self, sku, name, unit_price, stock_qty, category):
        self.sku = sku
        self.name = name
        self.unit_price = float(unit_price)
        self.stock_qty = int(stock_qty)
        self.category = category

    def remaining_stock(self, qty_sold: int) -> int:
        return self.stock_qty - qty_sold


class SaleTransaction:
    def __init__(self, sku, qty_sold, discount_pct, channel):
        self.sku = sku
        self.qty_sold = int(qty_sold)
        self.discount_pct = float(discount_pct)
        self.channel = channel

    def line_revenue(self, product):
        return compute_revenue(
            product.unit_price,
            self.qty_sold,
            self.discount_pct
        )
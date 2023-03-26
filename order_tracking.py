class Order:
    def __init__(self, order_id, product_name, status):
        self.order_id = order_id
        self.product_name = product_name
        self.status = status

class OrderTracker:
    def __init__(self):
        self.orders = []

    def add_order(self, order):
        self.orders.append(order)

    def get_order_by_id(self, order_id):
        for order in self.orders:
            if order.order_id == order_id:
                return order
        return None

    def update_order_status(self, order_id, new_status):
        order = self.get_order_by_id(order_id)
        if order is not None:
            order.status = new_status
            return True
        else:
            return False

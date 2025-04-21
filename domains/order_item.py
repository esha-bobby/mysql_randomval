class OrderItem:
    def __init__(self, order_id, order_item_id, product_id, seller_id, price, shipping_charges):
        self.order_id = order_id
        self.order_item_id = order_item_id
        self.product_id = product_id
        self.seller_id = seller_id
        self.price = price
        self.shipping_charges = shipping_charges

    def insert(self, db):
        try:
            db.cursor.execute("""
                INSERT INTO order_items (
                    order_id, order_item_id, product_id,
                    seller_id, price, shipping_charges
                ) VALUES (%s, %s, %s, %s, %s, %s)
            """, (
                self.order_id, self.order_item_id, self.product_id,
                self.seller_id, self.price, self.shipping_charges
            ))
        except:
            pass


import random
class OrderItem:
    def __init__(self, faker, order_id, product_id):
        self.order_id = order_id
        self.order_item_id = random.randint(1, 5)
        self.product_id = product_id
        self.seller_id = faker.bothify('SELL###')
        self.price = round(random.uniform(10.0, 1000.0), 2)
        self.shipping_charges = round(random.uniform(2.0, 50.0), 2)

    def insert(self, db):
        db.cursor.execute("""
            INSERT INTO order_items (
                order_id, order_item_id, product_id, seller_id,
                price, shipping_charges
            ) VALUES (%s, %s, %s, %s, %s, %s)
        """, (
            self.order_id, self.order_item_id, self.product_id,
            self.seller_id, self.price, self.shipping_charges
        ))

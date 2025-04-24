from faker import Faker
import random

fake = Faker()

class OrderItem:
    def __init__(self, order_id, product_id):
        self.order_id = order_id
        self.order_item_id = fake.unique.bothify('ITEM####') 
        self.product_id = product_id
        self.seller_id = fake.unique.bothify('SEL####')           
        self.price = round(random.uniform(5, 500), 2)
        self.shipping_charges = round(random.uniform(1, 50), 2)

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

import random
from datetime import timedelta

class Order:
    statuses = ['delivered', 'shipped', 'processing', 'canceled']

    def __init__(self, faker, customer_id):
        self.order_id = faker.unique.bothify('ORD####')
        self.customer_id = customer_id
        self.status = random.choice(Order.statuses)
        self.purchase_ts = faker.date_time_this_year()
        self.approved_at = self.purchase_ts + timedelta(minutes=random.randint(5, 120))
        self.delivered_ts = self.approved_at + timedelta(days=random.randint(1, 7))
        self.estimated_delivery = self.delivered_ts + timedelta(days=random.randint(1, 3))

    def insert(self, db):
        db.cursor.execute("""
            INSERT INTO orders (
                ORDER_ID, CUSTOMER_ID, ORDER_STATUS,
                ORDER_PURCHASE_TIMESTAMP, ORDER_APPROVED_AT,
                ORDER_DELIVERED_TIMESTAMP, ORDER_ESTIMATED_DELIVERY_DATE
            ) VALUES (%s, %s, %s, %s, %s, %s, %s)
        """, (
            self.order_id,
            self.customer_id,
            self.status,
            self.purchase_ts.strftime('%Y-%m-%d %H:%M:%S'),
            self.approved_at.strftime('%Y-%m-%d %H:%M:%S'),
            self.delivered_ts.strftime('%Y-%m-%d %H:%M:%S'),
            self.estimated_delivery.strftime('%Y-%m-%d')
        ))

class CustomerOrder:
    def __init__(self, customer_id, order_id):
        self.customer_id = customer_id
        self.order_id = order_id

    def insert(self, db):
        try:
            db.cursor.execute("""
                INSERT INTO customer_orders (
                    customer_id, order_id
                ) VALUES (%s, %s)
            """, (self.customer_id, self.order_id))
        except:
            pass


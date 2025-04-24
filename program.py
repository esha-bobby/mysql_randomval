from faker import Faker
import mysql.connector
from datetime import timedelta
import random


class Database:
    def __init__(self):
        self.con = mysql.connector.connect(
            host="localhost", user="eshaa",
            password="esha123", database="sales"
        )
        self.cursor = self.con.cursor()

    def commit_and_close(self):
        self.con.commit()
        self.cursor.close()
        self.con.close()

class Customer:
    genders = ['Male', 'Female', 'Other']

    def __init__(self, faker):
        self.data = (
            faker.unique.bothify('CUS####'),
            faker.postcode()[:5],
            faker.city(),
            faker.state_abbr(),
            random.choice(Customer.genders),
            random.randint(18, 80)
        )

    def insert(self, db):
        try:
            db.cursor.execute("""
                INSERT INTO customers (
                    customer_id, customer_zip_code_prefix,
                    customer_city, customer_state, gender, age
                ) VALUES (%s, %s, %s, %s, %s, %s)
            """, self.data)
        except mysql.connector.errors.IntegrityError:
            pass

class Order:
    statuses = ['delivered', 'shipped', 'processing', 'canceled']

    def __init__(self, faker, customer_id):
        self.order_id = faker.unique.bothify('ORD####')
        purchase = faker.date_time_this_year()
        approved = purchase + timedelta(minutes=random.randint(5, 120))
        delivered = approved + timedelta(days=random.randint(1, 7))
        estimated = delivered + timedelta(days=random.randint(1, 3))

        self.data = (
            self.order_id, customer_id,
            random.choice(Order.statuses),
            purchase.strftime('%Y-%m-%d %H:%M:%S'),
            approved.strftime('%Y-%m-%d %H:%M:%S'),
            delivered.strftime('%Y-%m-%d %H:%M:%S'),
            estimated.strftime('%Y-%m-%d')
        )

    def insert(self, db):
        db.cursor.execute("""
            INSERT INTO orders (
                ORDER_ID, CUSTOMER_ID, ORDER_STATUS,
                ORDER_PURCHASE_TIMESTAMP, ORDER_APPROVED_AT,
                ORDER_DELIVERED_TIMESTAMP, ORDER_ESTIMATED_DELIVERY_DATE
            ) VALUES (%s, %s, %s, %s, %s, %s, %s)
        """, self.data)

class Product:
    def __init__(self, faker):
        self.data = (
            faker.unique.bothify('PRD####'),
            faker.word().capitalize(),
            random.randint(100, 10000),
            random.randint(10, 100),
            random.randint(10, 100),
            random.randint(10, 100),
            round(random.uniform(10, 1000), 2),
            faker.word().capitalize() + " Product"
        )

    def insert(self, db):
        db.cursor.execute("""
            INSERT INTO products (
                product_id, product_category_name,
                product_weight_g, product_length_cm,
                product_height_cm, product_width_cm,
                product_cost, product_name
            ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """, self.data)

class OrderItem:
    def __init__(self, order_id, item_id, product_id, faker):
        self.data = (
            order_id, item_id, product_id,
            faker.unique.bothify('SEL####'),
            round(random.uniform(5, 500), 2),
            round(random.uniform(1, 50), 2)
        )

    def insert(self, db):
        try:
            db.cursor.execute("""
                INSERT INTO order_items (
                    order_id, order_item_id, product_id,
                    seller_id, price, shipping_charges
                ) VALUES (%s, %s, %s, %s, %s, %s)
            """, self.data)
        except mysql.connector.errors.IntegrityError:
            pass

class CustomerOrder:
    def __init__(self, customer_id, order_id):
        self.data = (customer_id, order_id)

    def insert(self, db):
        try:
            db.cursor.execute("""
                INSERT INTO customer_orders (customer_id, order_id)
                VALUES (%s, %s)
            """, self.data)
        except mysql.connector.errors.IntegrityError:
            pass
def main():
    fake = Faker()
    db = Database()

    customer_ids, order_ids, product_ids = [], [], []


    inserted = 0
    while inserted < 1000:
        c = Customer(fake)
        try:
            c.insert(db)
            customer_ids.append(c.data[0])
            inserted += 1
        except mysql.connector.errors.IntegrityError:
            pass

    inserted = 0
    while inserted < 500:
        p = Product(fake)
        try:
            p.insert(db)
            product_ids.append(p.data[0])
            inserted += 1
        except mysql.connector.errors.IntegrityError:
            pass

    inserted = 0
    while inserted < 1000:
        cust_id = random.choice(customer_ids)
        o = Order(fake, cust_id)
        try:
            o.insert(db)
            order_ids.append(o.data[0])
            CustomerOrder(cust_id, o.data[0]).insert(db)
            inserted += 1
        except mysql.connector.errors.IntegrityError:
            pass

    inserted = 0
    item_tracker = {}
    while inserted < 1000:
        order_id = random.choice(order_ids)
        item_tracker[order_id] = item_tracker.get(order_id, 0) + 1
        item = OrderItem(order_id, item_tracker[order_id], random.choice(product_ids), fake)
        try:
            item.insert(db)
            inserted += 1
        except mysql.connector.errors.IntegrityError:
            pass

    db.commit_and_close()
    print("All data inserted successfully")

main()

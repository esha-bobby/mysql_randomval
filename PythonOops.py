from faker import Faker
import mysql.connector
from datetime import timedelta
import random

class Database:
    def __init__(self):
        self.con = mysql.connector.connect(
            host="localhost",
            user="eshaa",
            password="esha123",
            database="sales"
        )
        self.cursor = self.con.cursor()

    def commit(self):
        self.con.commit()

    def close(self):
        self.cursor.close()
        self.con.close()

class Customer:
    genders = ['Male', 'Female', 'Other']

    def __init__(self, faker):
        self.customer_id = faker.unique.bothify('CUS####')
        self.zip_prefix = faker.postcode()[:5]
        self.city = faker.city()
        self.state = faker.state_abbr()
        self.gender = random.choice(Customer.genders)
        self.age = random.randint(18, 80)

    def insert(self, db):
        db.cursor.execute("""
            INSERT INTO customers (
                customer_id, customer_zip_code_prefix,
                customer_city, customer_state,
                gender, age
            ) VALUES (%s, %s, %s, %s, %s, %s)
        """, (
            self.customer_id, self.zip_prefix, self.city,
            self.state, self.gender, self.age
        ))

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

def main():
    fake = Faker()
    db = Database()
    customer_ids = []

    for _ in range(1000):
        customer = Customer(fake)
        customer.insert(db)
        customer_ids.append(customer.customer_id)

    for _ in range(1000):
        customer_id = random.choice(customer_ids)
        order = Order(fake, customer_id)
        order.insert(db)

    db.commit()
    db.close()
    print("1000 customers and 1000 orders inserted ")

main()

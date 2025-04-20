from faker import Faker
import random

from database import Database
from domain.customer import Customer
from orders.order import Order
from product.product import Product
from orderitems.OrderItem import OrderItem
from customerorder.CustomerOrder import CustomerOrder # type: ignore

def main():
    fake = Faker()
    db = Database()
    customer_ids = []
    order_ids = []
    product_ids = []

    # Insert products
    for _ in range(1000):  # You can change 100 to 1000
        product = Product(fake)
        product.insert(db)
        product_ids.append(product.product_id)

    # Insert customers
    for _ in range(1000):
        customer = Customer(fake)
        customer.insert(db)
        customer_ids.append(customer.customer_id)

    # Insert orders and order items
    for _ in range(1000):
        customer_id = random.choice(customer_ids)
        order = Order(fake, customer_id)
        order.insert(db)
        order_ids.append(order.order_id)

        # Link customer to order
        cust_order = CustomerOrder(customer_id, order.order_id)
        cust_order.insert(db)

        # Insert 1-3 items per order
        for _ in range(random.randint(1, 3)):
            product_id = random.choice(product_ids)
            item = OrderItem(fake, order.order_id, product_id)
            item.insert(db)

    db.commit()
    db.close()
    print("Data inserted successfully.")

from faker import Faker
import random


from domains.customer import Customer
from db.database import Database
from domains.product import Product
from domains.order import Order
from domains.order_item import OrderItem
from domains.customer_order import CustomerOrder

def main():
    fake = Faker()
    db = Database()

    customer_ids = []
    order_ids = []
    product_ids = []

    for _ in range(1000):
        customer = Customer(fake)
        customer.insert(db)
        customer_ids.append(customer.customer_id)

    for _ in range(500):
        product = Product(fake)
        product.insert(db)
        product_ids.append(product.product_id)

    for _ in range(1000):
        customer_id = random.choice(customer_ids)
        order = Order(fake, customer_id)
        order.insert(db)
        order_ids.append(order.order_id)

        customer_order = CustomerOrder(customer_id, order.order_id)
        customer_order.insert(db)


    for _ in range(1000):  
        order_id = random.choice(order_ids)
        product_id = random.choice(product_ids) 
        item = OrderItem(order_id, product_id) 
        item.insert(db)



    db.commit()
    db.close()
    print(" All data inserted successfully!")

if __name__ == '__main__':
    main()

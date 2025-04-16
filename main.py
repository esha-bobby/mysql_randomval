from faker import Faker
import random
from database import Database
from customer import Customer
from order import Order

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
    print("1000 customers and 1000 orders inserted.")

if __name__ == "__main__":
    main()

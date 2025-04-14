from faker import Faker
import mysql.connector
from datetime import timedelta
import random

con = mysql.connector.connect(
    host="localhost",
    user="eshaa",
    password="esha123",
    database="sales"
)
cursor = con.cursor()

fake = Faker()
statuses = ['delivered', 'shipped', 'processing', 'canceled']
genders = ['Male', 'Female', 'Other']


for _ in range(1000):
    customer_id = fake.unique.bothify('CUS####')
    customer_zip_code_prefix = fake.postcode()[:5]
    customer_city = fake.city()
    customer_state = fake.state_abbr()
    gender = random.choice(genders)
    age = random.randint(18, 80)

    cursor.execute("""
        INSERT INTO customers (
            customer_id, customer_zip_code_prefix,
            customer_city, customer_state,
            gender, age
        ) VALUES (%s, %s, %s, %s, %s, %s)
    """, (
        customer_id,
        customer_zip_code_prefix,
        customer_city,
        customer_state,
        gender,
        age
    ))



for _ in range(1000):
    order_id = fake.unique.bothify('ORD####')
    customer_id = fake.bothify('CUS####')  
    order_status = random.choice(statuses)
    order_purchase_timestamp = fake.date_time_this_year()
    order_approved_at = order_purchase_timestamp + timedelta(minutes=random.randint(5, 120))
    order_delivered_timestamp = order_approved_at + timedelta(days=random.randint(1, 7))
    order_estimated_delivery_date = order_delivered_timestamp + timedelta(days=random.randint(1, 3))

    cursor.execute("""
        INSERT INTO orders (
            ORDER_ID, CUSTOMER_ID, ORDER_STATUS,
            ORDER_PURCHASE_TIMESTAMP, ORDER_APPROVED_AT,
            ORDER_DELIVERED_TIMESTAMP, ORDER_ESTIMATED_DELIVERY_DATE
        ) VALUES (%s, %s, %s, %s, %s, %s, %s)
    """, (
        order_id,
        customer_id,
        order_status,
        order_purchase_timestamp.strftime('%Y-%m-%d %H:%M:%S'),
        order_approved_at.strftime('%Y-%m-%d %H:%M:%S'),
        order_delivered_timestamp.strftime('%Y-%m-%d %H:%M:%S'),
        order_estimated_delivery_date.strftime('%Y-%m-%d')
    ))

con.commit()
print(" 1000 customers and 1000 orders inserted successfully.")

cursor.close()
con.close()

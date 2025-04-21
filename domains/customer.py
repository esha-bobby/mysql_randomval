import random

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
        try:
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
        except:
            pass

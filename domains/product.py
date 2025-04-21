import random

class Product:
    def __init__(self, faker):
        self.product_id = faker.unique.bothify('PRD####')
        self.category = faker.word().capitalize()
        self.weight = random.randint(100, 10000)
        self.length = random.randint(10, 100)
        self.height = random.randint(10, 100)
        self.width = random.randint(10, 100)
        self.cost = round(random.uniform(10, 1000), 2)
        self.name = faker.word().capitalize() + " Product"

    def insert(self, db):
        db.cursor.execute("""
            INSERT INTO products (
                product_id, product_category_name,
                product_weight_g, product_length_cm,
                product_height_cm, product_width_cm,
                product_cost, product_name
            ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """, (
            self.product_id, self.category,
            self.weight, self.length,
            self.height, self.width,
            self.cost, self.name
        ))

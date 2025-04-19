import random


class Product:
    categories = ['Books', 'Electronics', 'Clothing', 'Beauty', 'Home']

    def __init__(self, faker):
        self.product_id = faker.unique.bothify('PROD####')
        self.product_name = faker.word().capitalize()
        self.product_category = random.choice(Product.categories)
        self.weight = random.randint(100, 3000)
        self.length = random.randint(5, 50)
        self.height = random.randint(1, 20)
        self.width = random.randint(1, 20)
        self.cost = round(random.uniform(5.0, 500.0), 2)

    def insert(self, db):
        db.cursor.execute("""
            INSERT INTO products (
                product_id, product_name, product_category_name,
                product_weight_g, product_length_cm,
                product_height_cm, product_width_cm, product_cost
            ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """, (
            self.product_id, self.product_name, self.product_category,
            self.weight, self.length, self.height, self.width, self.cost
        ))

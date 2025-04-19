create database sales;

CREATE TABLE orders (
    ORDER_ID VARCHAR(10) PRIMARY KEY,
    CUSTOMER_ID VARCHAR(10),
    ORDER_STATUS VARCHAR(20),
    ORDER_PURCHASE_TIMESTAMP DATETIME,
    ORDER_APPROVED_AT DATETIME,
    ORDER_DELIVERED_TIMESTAMP DATETIME,
    ORDER_ESTIMATED_DELIVERY_DATE DATE
);

CREATE TABLE customers (
    customer_id VARCHAR(10) PRIMARY KEY,
    customer_zip_code_prefix VARCHAR(10),
    customer_city VARCHAR(100),
    customer_state VARCHAR(10),
    gender VARCHAR(10),
    age INT
);
CREATE TABLE products (
    product_id VARCHAR(10) NOT NULL PRIMARY KEY,
    product_name VARCHAR(100),
    product_category_name VARCHAR(100),
    product_weight_g INT,
    product_length_cm INT,
    product_height_cm INT,
    product_width_cm INT,
    product_cost DECIMAL(10,2)
);
CREATE TABLE order_items (
    order_id VARCHAR(10),
    order_item_id INT,
    product_id VARCHAR(10),
    seller_id VARCHAR(10),
    price DECIMAL(10,2),
    shipping_charges DECIMAL(10,2),
    PRIMARY KEY (order_id, order_item_id),
    FOREIGN KEY (order_id) REFERENCES orders(order_id),
    FOREIGN KEY (product_id) REFERENCES products(product_id)
);
CREATE TABLE customer_orders (
    customer_order_id INT AUTO_INCREMENT PRIMARY KEY,
    customer_id VARCHAR(10),
    order_id VARCHAR(10),
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id),
    FOREIGN KEY (order_id) REFERENCES orders(order_id)
);


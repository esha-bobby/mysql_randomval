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
    product_id VARCHAR(10) PRIMARY KEY,
    product_name VARCHAR(100),
    product_category_name VARCHAR(100),
    product_weight_g INT,
    product_length_cm INT,
    product_height_cm INT,
    product_width_cm INT,
    product_cost DECIMAL(10,2)
);


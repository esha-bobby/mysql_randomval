CREATE DATABASE IF NOT EXISTS sales;
USE sales;

-- Customers table
CREATE TABLE customers (
    customer_id VARCHAR(10) PRIMARY KEY,
    customer_zip_code_prefix VARCHAR(10),
    customer_city VARCHAR(255),
    customer_state VARCHAR(10),
    gender ENUM('Male', 'Female', 'Other'),
    age INT
);

-- Products table
CREATE TABLE products (
    product_id VARCHAR(10) PRIMARY KEY,
    product_category_name VARCHAR(255),
    product_weight_g INT,
    product_length_cm INT,
    product_height_cm INT,
    product_width_cm INT,
    product_cost DECIMAL(10,2),
    product_name VARCHAR(255)
);

-- Orders table
CREATE TABLE orders (
    order_id VARCHAR(10) PRIMARY KEY,
    customer_id VARCHAR(10),
    order_status ENUM('delivered', 'shipped', 'processing', 'canceled'),
    order_purchase_timestamp DATETIME,
    order_approved_at DATETIME,
    order_delivered_timestamp DATETIME,
    order_estimated_delivery_date DATE
);

-- Order Items table
CREATE TABLE order_items (
    order_id VARCHAR(10),
    order_item_id VARCHAR(15) PRIMARY KEY,
    product_id VARCHAR(10),
    seller_id VARCHAR(10),
    price DECIMAL(10,2),
    shipping_charges DECIMAL(10,2)
);

-- Customer Orders linking table
CREATE TABLE customer_orders (
    customer_id VARCHAR(10),
    order_id VARCHAR(10),
    PRIMARY KEY (customer_id, order_id)
);

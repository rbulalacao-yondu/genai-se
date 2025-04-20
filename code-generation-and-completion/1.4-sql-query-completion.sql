-- Top 5 customers by revenue
SELECT customer_id, SUM(total_amount) AS total_revenue
FROM orders
GROUP BY customer_id
ORDER BY total_revenue DESC
LIMIT 5;


-- Schema of orders table
CREATE TABLE orders (
     order_id INT PRIMARY KEY,
     customer_id INT,
     order_date DATE,
     total_amount DECIMAL(10, 2)
);

-- Insert sample data into orders table
INSERT INTO orders (order_id, customer_id, order_date, total_amount) VALUES
(1, 101, '2023-01-01', 150.00),
(2, 102, '2023-01-02', 200.00),
(3, 101, '2023-01-03', 300.00),
(4, 103, '2023-01-04', 250.00),
(5, 102, '2023-01-05', 400.00),
(6, 101, '2023-01-06', 500.00),
(7, 104, '2023-01-07', 600.00),
(8, 105, '2023-01-08', 700.00),
(9, 106, '2023-01-09', 800.00),
(10, 107, '2023-01-10', 900.00);
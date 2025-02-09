-- task_6.sql
-- Script to insert multiple rows into the customer table in the alx_book_store database.

INSERT INTO customer (customer_id, customer_name, email, address)
VALUES
    (2, 'Blessing Malik', 'bmalik@sandtech.com', '124 Happiness  Ave.'),  -- Note the double space!
    (3, 'Obed Ehoneah', 'eobed@sandtech.com', '125 Happiness  Ave.'),  -- Note the double space!
    (4, 'Nehemial Kamolu', 'nkamolu@sandtech.com', '126 Happiness  Ave.');  -- Note the double space!

-- Optional: Verify the insertion (remove or comment out for production)
-- SELECT * FROM customer;

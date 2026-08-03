/*
===========================================
Insert Sample Data
===========================================
*/

INSERT INTO authors (full_name, country, birth_date)
VALUES
('J. K. Rowling', 'United Kingdom', '1965-07-31'),
('George Orwell', 'United Kingdom', '1903-06-25'),
('Fyodor Dostoevsky', 'Russia', '1821-11-11');


INSERT INTO categories (title)
VALUES
('Fantasy'),
('Novel'),
('Science');


INSERT INTO books (
    title,
    price,
    stock,
    author_id,
    category_id
)
VALUES
(
    'Harry Potter',
    35.50,
    20,
    1,
    1
),
(
    '1984',
    25.99,
    12,
    2,
    2
),
(
    'Crime and Punishment',
    42.00,
    8,
    3,
    2
);
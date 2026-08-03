/*
===========================================
Subqueries
===========================================
*/

------------------------------------------------
-- کتاب‌هایی که قیمتشان از میانگین بیشتر است
------------------------------------------------

SELECT
    title,
    price
FROM books
WHERE price >
(
    SELECT AVG(price)
    FROM books
);

------------------------------------------------
-- کتاب‌های نویسنده George Orwell
------------------------------------------------

SELECT
    title
FROM books
WHERE author_id =
(
    SELECT id
    FROM authors
    WHERE full_name = 'George Orwell'
);

------------------------------------------------
-- کتاب‌های دسته‌بندی Fantasy
------------------------------------------------

SELECT
    title
FROM books
WHERE category_id =
(
    SELECT id
    FROM categories
    WHERE title = 'Fantasy'
);

------------------------------------------------
-- نویسنده‌هایی که حداقل یک کتاب دارند
------------------------------------------------

SELECT *
FROM authors
WHERE id IN
(
    SELECT author_id
    FROM books
);

------------------------------------------------
-- دسته‌بندی‌هایی که هیچ کتابی ندارند
------------------------------------------------

SELECT *
FROM categories
WHERE id NOT IN
(
    SELECT category_id
    FROM books
);
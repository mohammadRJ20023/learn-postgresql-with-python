SELECT
    authors.full_name,
    books.title
FROM authors
LEFT JOIN books
    ON authors.id = books.author_id;
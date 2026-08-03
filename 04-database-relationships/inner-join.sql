SELECT

    books.title,

    authors.full_name,

    categories.title

FROM books

INNER JOIN authors
ON books.author_id = authors.id

INNER JOIN categories
ON books.category_id = categories.id;
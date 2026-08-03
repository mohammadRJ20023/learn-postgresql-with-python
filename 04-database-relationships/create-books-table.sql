/*
===========================================
Create Books Table
===========================================
*/

CREATE TABLE books (

    id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,

    title VARCHAR(200) NOT NULL,

    price NUMERIC(10,2) NOT NULL,

    stock INTEGER DEFAULT 0,

    author_id INTEGER NOT NULL,

    category_id INTEGER NOT NULL,

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT fk_books_author
        FOREIGN KEY (author_id)
        REFERENCES authors(id),

    CONSTRAINT fk_books_category
        FOREIGN KEY (category_id)
        REFERENCES categories(id)

);
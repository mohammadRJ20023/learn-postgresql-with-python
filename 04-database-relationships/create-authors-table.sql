/*
===========================================
Create Authors Table
===========================================
*/

CREATE TABLE authors (

    id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,

    full_name VARCHAR(150) NOT NULL,

    country VARCHAR(100),

    birth_date DATE,

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP

);
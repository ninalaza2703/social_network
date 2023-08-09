DROP TABLE users CASCADE;

--DROP TABLE IF EXISTS users;
CREATE TABLE users (
    id integer PRIMARY KEY,
    surname varchar(255),
    name varchar(255),
    age integer,
    subscription_date TIMESTAMP
);

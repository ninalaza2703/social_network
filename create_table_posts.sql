DROP TABLE IF EXISTS posts;

CREATE TABLE posts (
    post_id SERIAL PRIMARY KEY,
    user_id integer REFERENCES users(id),
    post_type varchar(255),
    post_date TIMESTAMP
);
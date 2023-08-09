DROP TABLE IF EXISTS reactions;

CREATE TABLE reactions (
    reaction_id serial PRIMARY KEY,
    user_id integer REFERENCES users(id),
    reaction_type varchar(255),
    reaction_date TIMESTAMP
);
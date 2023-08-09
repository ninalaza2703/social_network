DROP TABLE IF EXISTS friends;

CREATE TABLE friends (
    friend_1 integer,
    friend_2 integer,
    PRIMARY KEY (friend_1, friend_2),
    FOREIGN KEY (friend_1) REFERENCES users (id),
    FOREIGN KEY (friend_2) REFERENCES users (id)
);


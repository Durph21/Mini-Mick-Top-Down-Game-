DROP TABLE IF EXISTS leader_board;

CREATE TABLE leader_board
(
    user_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    score TEXT NOT NULL
    
);
INSERT INTO leader_board (name, score)
VALUES ('Darragh', '837');


SELECT *
FROM leader_board;
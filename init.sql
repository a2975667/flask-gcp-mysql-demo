CREATE DATABASE todo;
USE todo;
CREATE TABLE tasks (
    id int NOT NULL AUTO_INCREMENT,
    task varchar(255) NOT NULL,
    status char(30),
    PRIMARY KEY (id)
);
INSERT INTO tasks (task, status) VALUES ("Task no.1" , "Todo");
INSERT INTO tasks (task, status) VALUES ("Task no.2" , "Todo");
INSERT INTO tasks (task, status) VALUES ("Task no.3" , "Todo");


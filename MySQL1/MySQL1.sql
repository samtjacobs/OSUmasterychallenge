# Create database
CREATE DATABASE ex_db;
USE ex_db;
# Create Table
CREATE TABLE ex_tab (id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
name VARCHAR(20),
age INT,
dateandtime DATETIME NOT NULL DEFAULT NOW(),
commentbox VARCHAR(256));
# Add entries
INSERT INTO `ex_tab` (`id`,`name`,`age`,`commentbox`)
VALUES (NULL, "John", 20, "First Entry");
INSERT INTO `ex_tab` (`id`,`name`,`age`,`commentbox`)
VALUES (NULL, "Jack", 23, "Second Entry");
INSERT INTO `ex_tab` (`id`,`name`,`age`,`commentbox`)
VALUES (NULL, "Jill", 39, "Third Entry");
# Save
SELECT * FROM `ex_tab`;

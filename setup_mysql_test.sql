-- create database 
CREATE DATABASE IF NOT EXISTS hbnb_test_db;
-- CREATE user hbnb_test
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';
-- grant hbnb_test all privilges on hbnb_test_db
GRANT ALL ON hbnb_test_db.* TO 'hbnb_test'@'localhost';
-- grant hbnb_test SELECT privilges on performance_schema
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';

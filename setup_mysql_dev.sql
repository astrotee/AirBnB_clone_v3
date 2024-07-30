-- create database 
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
-- CREATE user hbnb_dev
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
-- grant hbnb_dev all privilges on hbnb_dev_db
GRANT ALL ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';
-- grant hbnb_dev SELECT privilges on performance_schema
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';

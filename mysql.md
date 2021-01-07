Both scripts rely on a MySQL database. It uses following tables:

CREATE DATABASE hardcoded_dbname;
GRANT ALL PRIVILEGES ON *.* TO 'cbuser' @'%';
 
CREATE TABLE staff (
vm_name VARCHAR(30) PRIMARY KEY NOT NULL,
email VARCHAR(50) NOT NULL,
team_name VARCHAR(30) NOT NULL,
as_enabled VARCHAR(1),
flag VARCHAR(30),
reg_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);
 
create table schedule (
id INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY,
team_name VARCHAR(30) NOT NULL,
dow INT(1),
shift VARCHAR(1),
as_time INT(4),
reg_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

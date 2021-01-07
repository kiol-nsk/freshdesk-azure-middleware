Scripts rely on a MySQL database (any DB can be used).
Database currently manually maintained.

MySQL [cb]> desc staff;
+------------+-------------+------+-----+-------------------+-----------------------------+
| Field      | Type        | Null | Key | Default           | Extra                       |
+------------+-------------+------+-----+-------------------+-----------------------------+
| vm_name    | varchar(30) | NO   | PRI | NULL              |                             |
| email      | varchar(50) | NO   |     | NULL              |                             |
| team_name  | varchar(30) | NO   |     | NULL              |                             |
| as_enabled | varchar(1)  | YES  |     | NULL              |                             |
| flag       | varchar(30) | YES  |     | NULL              |                             |
| reg_date   | timestamp   | NO   |     | CURRENT_TIMESTAMP | on update CURRENT_TIMESTAMP |
+------------+-------------+------+-----+-------------------+-----------------------------+
6 rows in set (0.24 sec)

MySQL [cb]> desc schedule;
+-----------+-----------------+------+-----+-------------------+-----------------------------+
| Field     | Type            | Null | Key | Default           | Extra                       |
+-----------+-----------------+------+-----+-------------------+-----------------------------+
| id        | int(6) unsigned | NO   | PRI | NULL              | auto_increment              |
| team_name | varchar(30)     | NO   |     | NULL              |                             |
| dow       | int(1)          | YES  |     | NULL              |                             |
| shift     | varchar(1)      | YES  |     | NULL              |                             |
| as_time   | varchar(4)      | YES  |     | NULL              |                             |
| reg_date  | timestamp       | NO   |     | CURRENT_TIMESTAMP | on update CURRENT_TIMESTAMP |
+-----------+-----------------+------+-----+-------------------+-----------------------------+
6 rows in set (0.00 sec)

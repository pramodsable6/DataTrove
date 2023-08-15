# mysql terminal commands
```shell
brew install mysql
mysql.server start
mysql -u root  # (login without password for the first time)
mysql_secure_installation
mysql -u root -p  # (login with password)
```

----

# queries
```

-- To change password for root user
ALTER USER 'root'@'localhost' IDENTIFIED BY 'NewPassword@123';

-- To create a database
create database db_name;

-- Show databases
show databases;

-- Use a database
use database;

-- Show tables in a database
show tables;
```

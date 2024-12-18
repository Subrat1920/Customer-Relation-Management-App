## install MySQL on your computer
## https://dev.mysql.com/downloads/installer/
## pip install mysql
## pip install mysql-connector
## pip install mysql-connector-python

import mysql.connector


dataBase = mysql.connector.connect(
    host="localhost",
    user = 'root',
    password = 'Subuking@2000'
)

cursorObject = dataBase.cursor()

## creating a database
cursorObject.execute("CREATE DATABASE crm")




print('All Done')
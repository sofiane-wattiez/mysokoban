import pymysql
# This files contains my test method to insert data into the database with the pymysql module>

# ok : this part working fine
# conn = pymysql.connect(host='127.0.0.1', user='root', password='', charset='utf8', db='sokoban')
# cur = conn.cursor()

conn = pymysql.connect(host='127.0.0.1', user='root', password='', charset='utf8', db='sokoban')
cur = conn.cursor()
sql =   """insert into `player` (playerName, levelScore) values ( %s , %s)"""
cur.execute(sql,( 'morgan', 11))
conn.commit()

# databaseServerIP            = "127.0.0.1"  # IP address of the MySQL database server
# databaseUserName            = "root"       # User name of the database server
# databaseUserPassword        = ""           # Password for the database user
# newDatabaseName             = "Sokoban" # Name of the database that is to be created
# charSet                     = "utf8mb4"     # Character set
# cusrorType = pymysql.cursors.DictCursor
# connectionInstance   = pymysql.connect(host=databaseServerIP, user=databaseUserName, password=databaseUserPassword,
# charset=charSet,cursorclass=cusrorType)
# try:


# ok : this part working fine
# Id from player table in database being auto-incremented
# cur.execute("INSERT INTO `player` ( playerName, playerScore) VALUES (%s , %s)")
# sql =   """insert into `player` (playerName, playerScore) values ( %s , %s)"""
# cur.execute(sql,( 'lenny', 10))
# conn.commit()

#     sql =   """insert into `player` (playerName, playerScore) values ( %s , %s)"""
#     cur.execute(sql,( 'lenny', 1))
#     conn.commit()
#     #TEST PART OF THE CODE

#     # SQL query string
#     sqlQuery            = "select * from `player`"
#     # Execute the sqlQuery
#     cursorInsatnce.execute(sqlQuery)
#     insertPlayer                = cursorInsatnce.fetchall()

#     for insert in insertPlayer:
#         print(insert)

# except Exception as e:

#     print("Exeception occured:{}".format(e))

# finally:

#     connectionInstance.close()

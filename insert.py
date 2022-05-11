import pymysql

conn = pymysql.connect(host='127.0.0.1', user='root', password='', charset='utf8', db='sokoban')
cur = conn.cursor()

# Id from player table in database being auto-incremented
sql =   """   insert into `player` (playerName, playerScore) values ( %s , %s)"""
cur.execute(sql,( 'sofiane', 1))
conn.commit()
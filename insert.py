import pymysql
# This files contains my test method to insert data into the database with the pymysql module>

# ok : this part working fine
# conn = pymysql.connect(host='127.0.0.1', user='root', password='', charset='utf8', db='sokoban')
# cur = conn.cursor()



def insert():
    conn = pymysql.connect(host='127.0.0.1', user='root', password='', charset='utf8', db='sokoban')
    cur = conn.cursor()
    sql =   """insert into `player` (playerName, levelScore) values ( %s , %s)"""
    cur.execute(sql,( 'marina', 12))
    conn.commit()

if __name__ == '__main__':
    insert()
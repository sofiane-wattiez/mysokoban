import pymysql

conn = pymysql.connect(host='localhost', user='root', password='1234', charset='utf8', db='kobis')
cur = conn.cursor()

sql = """insert into `sokoban` (targetDt, rank, rankOldAndNew, 
                                  movieCd, movieNm, salesAmt, audiCnt)
         values (%s, %s, %s, %s, %s, %s, %s) 
    """
cur.execute(sql,(20180220,11,'OLD',20170511,'Conan',36388900,48011))
conn.commit()
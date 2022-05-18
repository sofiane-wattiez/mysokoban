import pymysql
# This files contains my test method to insert data into the database with the pymysql module>

# Le script insert() fonctionne utilisé "python ./insert.py" cependant pour envoyé une information en bdd via le reste du script mais je n'ai pas encore bien géré  mes [Key] et [Value]
# dans le reste de mon jeux.

def insert():
    score_level = 0
    # Décommenté prochaine ligne pour demander nom a l'utilisateur le via terminal
    # name = input("Enter your name: ")
    name = "marina"
    if score_level > 0:
        score_level += 1
        conn = pymysql.connect(host='127.0.0.1', user='root', password='', charset='utf8', db='sokoban')
        cur = conn.cursor()
        sql =   """insert into `player` (playerName, levelScore) values ( %s , %s)"""
        cur.execute(sql,( name, score_level))
        conn.commit()
    print("You win you'r return to :{} lvl".format(score_level))

if __name__ == '__main__':
    insert()
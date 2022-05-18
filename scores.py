import json
import pymysql
import os
import winreg

class Scores:
    def __init__(self, game):
        self.game = game
        # self.score = score
        # self.name = input("Enter your name: ")

    def load(self):
        try:
            with open("scores", "r") as data:
                scores = json.load(data)
                self.game.index_level = scores["level"]
            self.game.load_level()
            self.game.start()
        except FileNotFoundError:
            print("No saved data")

    # def insert(self):
        

    def save(self): 
        
        self.score = self.game.player.score
        if saved_level > 0:
            self.name = input("Enter your name: ")
            try:
                conn = pymysql.connect(host='127.0.0.1', user='root', password='', charset='utf8', db='sokoban')
                cur = conn.cursor()
                sql =   """insert into `player` (playerName, levelScore) values ( %s , %s)"""
                val = {'playerName': self.name, 'levelScore': self.score}
                cur.execute(sql,(val ))
                conn.commit()
            except Exception as e:
                saved_level = 0
                print("You loose you'r return to :{} lvl".format(e))




    # def save(self):
    #     # Saving score in file only when current level > saved level
    #     try:
    #         with open("scores", "r") as data:
    #             scores = json.load(data)
    #             saved_level = scores["level"]
    #     except FileNotFoundError:
    #         saved_level = 0

    #     if saved_level < self.game.index_level:
    #         data = {
    #             "level": self.game.index_level
    #         }
    #         with open("scores", "w") as scores:
    #             json.dump(data, scores, ensure_ascii=False, indent=4)

def insert():
    conn = pymysql.connect(host='127.0.0.1', user='root', password='', charset='utf8', db='sokoban')
    cur = conn.cursor()
    sql =   """insert into `player` (playerName, levelScore) values ( %s , %s)"""
    cur.execute(sql,( 'marina', 12))
    conn.commit()

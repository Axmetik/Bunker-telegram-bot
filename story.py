#імпорт бібліотеки random та курсору бази даних
from database import mycursor
import random

#Створення класу історія
class story():
    #Конструктор класу історія
    def __init__(self):
        self.story_ = ' '

    #Метод(гетер) історії
    def getStory(self):
        mycursor.execute('select * from story')
        self.story_ = random.choice(mycursor.fetchall())[1]
        return self.story_



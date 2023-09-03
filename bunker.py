#імпорт бібліотеки random та курсору бази даних
import random
from database import mycursor

#Створення класу бункер
class bunker():
    #Конструктор класу бункер
    def __init__(self):
        self.place = ' '
        self.square = ' '
        self.food = ' '

    #Метод вибору місця
    def setPlace(self):
        mycursor.execute('select * from bunker_')
        self.place = random.choice(mycursor.fetchall())[1]

    #Метод вибору площі бункера
    def setSquare(self):
        mycursor.execute('select * from bunker_')
        self.square = random.choice(mycursor.fetchall())[2]
    #Метод вибору кількості їжі
    def setFood(self):
        mycursor.execute('select * from bunker_')
        self.food = random.choice(mycursor.fetchall())[3]

    #Метод ствопення бункеру
    def setBunker(self):
        self.setPlace()
        self.setSquare()
        self.setFood()

    #Метод отримання бункеру на вивід
    def getBunker(self):
        bunker_ ="""
{0}
{1}
{2}
        """.format(self.place, self.square, self.food)
        return bunker_


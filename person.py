#імпорт бібліотеки random та курсору бази даних
import random
from database import mycursor

sex = ['Чоловік', 'Жінка']
kids_d_46 = ['Може мати дітей', 'Може мати дітей', 'Може мати дітей', 'Не може мати дітей']
kids_u_46_to_55 = ['Може мати дітей', 'Не може мати дітей', 'Не може мати дітей']

#Створення класу персони
class person():
    # Конструктор класу персони
    def __init__(self):
        self.sex = ' '
        self.age = 0
        self.profession = ' '
        self.illness = ' '
        self.invalid = ' '
        self.kids = ' '
        self.phobia = ' '
        self.character = ' '
        self.skill = ' '
        self.religion = ' '
        self.addition = ' '
        self.inventar = ' '
        self.card1 = ' '
        self.card2 = ' '

    # Метод вибору навичок
    def setSkills(self):
        mycursor.execute('select * from skills')
        self.skill = random.choice(mycursor.fetchall())[1]

    # Метод вибору професії
    def setProfession(self):
        mycursor.execute('select * from profession')
        self.profession = random.choice(mycursor.fetchall())[1]

    # Метод вибору інвалідності
    def setInvalid(self):
        mycursor.execute('select * from invalid')
        self.invalid = random.choice(mycursor.fetchall())[1]

    # Метод вибору хвороби
    def setIllness(self):
        mycursor.execute('select * from illness')
        self.illness = random.choice(mycursor.fetchall())[1]

    # Метод вибору багажу
    def setInventar(self):
        mycursor.execute('select * from inventar')
        self.inventar = random.choice(mycursor.fetchall())[1]

    # Метод вибору додаткової інформації
    def setAddition(self):
        mycursor.execute('select * from addition')
        self.addition = random.choice(mycursor.fetchall())[1]

    # Метод вибору релігія
    def setReligion(self):
        mycursor.execute('select * from religion')
        self.religion = random.choice(mycursor.fetchall())[1]

    # Метод вибору карти дії №1
    def setCard1(self):
        mycursor.execute('select * from cards')
        self.card1 = random.choice(mycursor.fetchall())[1]

    # Метод вибору карти дії №2
    def setCard2(self):
        mycursor.execute('select * from cards')
        self.card2 = random.choice(mycursor.fetchall())[1]

    # Метод вибору риси характеру
    def setCharacteristics(self):
        mycursor.execute('select * from characteristics')
        self.character = random.choice(mycursor.fetchall())[1]

    # Метод вибору фобії
    def setPhobias(self):
        mycursor.execute('select * from phobias')
        self.phobia = random.choice(mycursor.fetchall())[1]

    # Метод вибору віку персони
    def setAge(self):
        self.age = random.randint(17, 99)

    def setSex(self):
        self.sex = random.choice(sex)

    def setKids(self):
        if self.age <= 46:
            self.kids = random.choice(kids_d_46)
        elif self.age > 46 and self.age < 55:
            self.kids = random.choice(kids_u_46_to_55)
        elif self.age < 55 and self.illness == 'Абсолютно здоровий':
            self.kids = 'Може мати дітей'
        else:
            self.kids = 'Не може мати дітей'

    # Метод створення персони
    def setPerson(self):
        self.setSex()
        self.setAge()
        self.setProfession()
        self.setIllness()
        self.setInvalid()
        self.setKids()
        self.setCharacteristics()
        self.setPhobias()
        self.setSkills()
        self.setAddition()
        self.setInventar()
        self.setCard1()
        self.setCard2()
        self.setReligion()

    # Метод(гетера) отримання персони
    def getPerson(self):
        persona = """
🚻Стать: {0}
🎂Вік: {1}
🔧Професія: {2}
💟Стан здоров'я: {3}
♿Інвалідність: {4}
🚼Можливість мати дітей: {5}
☀Характер: {6}
🛐Релігія: {7}
🙈Фобія: {8}
⛳Хобі/вміння: {9}
➕Додаткова інформація: {10}
🎒Багаж: {11}
🃏Карта дії №1: {12}
🃏Карта дії №2: {13}  
        """.format(self.sex, self.age, self.profession, self.illness, self.invalid, self.kids, self.character,
                   self.religion, self.phobia, self.skill, self.addition, self.inventar, self.card1, self.card2)
        return persona




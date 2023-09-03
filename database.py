#імпорт конектора для бази даних
import mysql.connector

#Під'єднання бази даних
mydb = mysql.connector.connect(
    host='localhost',
    password='3835',
    user='root',
    database='bunker'
)

#Створення курсору для виконання дій над базою даних
mycursor = mydb.cursor()
import datetime
import telebot

while True:
    a = open("users.txt", "r")
    b = open("errors.txt", "a")
    c = a.readline()
    b.write(c)
    a.close()
    b.close()

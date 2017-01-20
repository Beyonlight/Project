# coding=utf8

import serial
import csv
ser = serial.Serial('/dev/ttyACM0', 9600)
fichier = open('data.csv', 'a')
wr = csv.writer(fichier)
for i in range(50):
    test = str(ser.readline())
    fichier.write(test)
    print(test)
fichier.close()


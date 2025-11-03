from datetime import datetime
import time
import random
import os
import serial

baudrate = 9600

def gps_emaulate():
        with open('gps.txt', "r", encoding="utf8") as file:
                lines = file.read().splitlines()
                file.close
        port = lines[0]
        ser = serial.Serial(port, baudrate)        
        coor_maps_n = lines[1]
        print(coor_maps_n + '  -в десятичных градусах из Yandex Map')
        coor_n1, coor_n2 = coor_maps_n.split(".", 1)
        coor_maps_e = lines[2]
        print(coor_maps_e + '  -в десятичных градусах из Yandex Map')
        coor_e1, coor_e2 = coor_maps_e.split(".", 1)
        print(coor_n1)
        print(coor_n2)
        print(coor_e1)
        print(coor_e2)
        coor_gps_n = coor_n1 + str(60 * (float(coor_maps_n) - int(coor_n1)))
        coor_gps_e = coor_e1 + str(60 * (float(coor_maps_e) - int(coor_e1)))
        print(coor_gps_n + '  -градусах и минутах в формате GPS')
        print(coor_gps_e + '  -градусах и минутах в формате GPS')
        coor_gps_n = round(float(coor_gps_n), 3)
        coor_gps_e = round(float(coor_gps_e), 3)
        print("после округления float")
        print(str(coor_gps_n) + '  -градусах и минутах в формате GPS')
        print(str(coor_gps_e) + '  -градусах и минутах в формате GPS')
        print("до проверки len")        
        print(len(str(coor_gps_n)))        
        print(len(str(coor_gps_e)))
              
        if len(str(coor_gps_n)) < 8:
                coor_gps_n = '0' + str(coor_gps_n)
        else: print ('.')
        if len(str(coor_gps_e)) < 8:
                coor_gps_e = '0' + str(coor_gps_e)
        else: print ('.')
        if len(str(coor_gps_n)) < 8:
                coor_gps_n = '0' + str(coor_gps_n)
        else: print ('.')
        if len(str(coor_gps_e)) < 8:
                coor_gps_e = '0' + str(coor_gps_e)
        else: print ('.')
        
        print(len(str(coor_gps_n)))
        print(len(str(coor_gps_e)))
        while True:
                current_time = datetime.utcnow()
                coor_time = (str(current_time.hour) + str(current_time.minute)
                      + str(current_time.second) + ".000")
                rand1 = random.randint(10, 99)
                rand2 = random.randint(10, 99)
                gpgll = ("$GPGLL," + str(coor_gps_n) + str(rand1) + ",N," + "0" +
                         str(coor_gps_e) + str(rand2) + ",E," + coor_time + ",A,A*6F\r\n")
                print(gpgll)
                ser.write(gpgll.encode('utf-8'))
                time.sleep(1)
        else:
                ser.close()
                print("Serial connection closed COM in " + port)

gps_emaulate()

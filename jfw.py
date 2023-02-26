import os
import sys
import time
import serial
import esptool


class Jfw:
    def __init__(self, porta, baud, firmware_path):
        self._port = porta
        self._baud = baud
        self._serial = serial.Serial(porta, baud)
        self._esp = esptool.ESP32Serial(porta, baud=baud)
        self._firmware_path = firmware_path 
       
 
        def flash(self):
            self._esp.baud = 460800
            self._esp.before_connect()
            self._esp.connect()
            self._esp.flash_file(self.firmware_path, 0x1000)
            self._esp.hard_reset()
            self._serial.close()
            
           
myesp = Jfw('COM6', 115200, 'C:\\Users\\erick\\Downloads\\esp32-20220618-v1.19.1.bin')
myesp.flash()
           
'''
Como deve funcionar:
meu_esp = Jfw('\dev\ttyUSB0', 115200, '\\User\\Desktop\\firmware.bin')
meu_esp.flash
att: não testado
'''

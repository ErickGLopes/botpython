import os
import sys
import time
import serial
import esptool


class Jfw:
    def __init__(self, porta, baud, firmware_path):
        self._port = porta
        self._baud = baud
        self._serial = serial.Serial(_port, _baud)
        self._esp = esptool.ESP32Serial(_port, baud=_baud)
        self._firmware_path = firmware_path 
       
        @property
        def flash(self):
            self._esp.baud = 460800
            self._esp.before_connect()
            self._esp.connect()
            self._esp.flash_file(_firmware_path, 0x1000)
            self._esp.hard_reset()
            self._serial.close()
            
            
'''
Como deve funcionar:

meu_esp = Jfw('\dev\ttyUSB0', 115200, '\\User\\Desktop\\firmware.bin')
meu_esp.flash

att: não testado
'''
 

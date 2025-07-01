import sys
import threading

from TCS34725.connectors.i2c import I2C

class TCS34725():
    def __init__(self, bus_number, address):
        self.i2c = I2C(bus_number, address)
    
    def enable(self):
        self.i2c.write_byte(0x00, 0x03)

    def read_corolor(self):
        clear = (self.i2c.read_byte(0x14)) | (self.i2c.read_byte(0x15) << 8)
        
    


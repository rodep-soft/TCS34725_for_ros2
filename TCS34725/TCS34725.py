from tcs34725.connectors.i2c import I2C

class TCS34725():
    def __init__(self, bus_number, address):
        self.i2c = I2C(bus_number, address)
    
    def enable(self):
        self.i2c.write_byte(0b10000000, 0x03)

    def read_colors(self):
        data = self.i2c.read_block_data(0b10100000|0x14, 8)
        c = (data[1] << 8) | data[0]
        r = (data[3] << 8) | data[2]
        g = (data[5] << 8) | data[4]
        b = (data[7] << 8) | data[6]
        return c, r, g, b
        
        
    


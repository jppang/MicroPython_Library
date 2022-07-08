from machine import Pin, SoftI2C

class TOF10120:
    
    def __init__(self, scl, sda, addr=82):
        self.scl = scl
        self.sda = sda
        self.i2c = SoftI2C(scl=Pin(self.scl), sda=Pin(self.sda))
        self.addr = addr
        self.measure()
        self.distance
        
    def measure(self):
        buf = bytearray(2)
        self.i2c.writeto(self.addr, 'r6#')
        buf = self.i2c.readfrom(self.addr, 2)
        self.distance = buf[0]<<8 | buf[1]
        return self.distance


def demo():
    tof = TOF10120(27, 26)
    distance = tof.measure()
    print(distance)

if __name__ == "__main__":
    demo()

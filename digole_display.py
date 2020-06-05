from machine import UART
from time import sleep_ms
from ubinascii import unhexlify

class DigoleDisplay:
    def __init__(self, serial=1, baud=9600, width=240, height=320):
        self.width = width
        self.height = height

        #configure serial
        self.uart = UART(serial, 9600)
        self.uart.init(9600, bits=8, parity=None, stop=1)
        sleep_ms(100)
        if baud != 9600:
            self.uart.write("SB" + str(baud))
            sleep_ms(100)
            self.uart = UART(serial, baud)
            self.uart.init(baud, bits=8, parity=None, stop=1)
            sleep_ms(100)
            self.uart.write("CL")
            sleep_ms(100)
        self.uart.write("CL")
        sleep_ms(100)

    def write2B(self, v):
        if v < 255:
            self.uart.write(hex(v))
        else:
            self.uart.write(hex(255))
            self.uart.write(hex(v - 255))

    def brightness(self, i):
        v = str(i)
        if len(v) < 2:
            v ="0" + v
        self.uart.write("BL")
        self.uart.write(unhexlify(''.join(v)))

    def backLightOff(self):
        self.brightness(0)

    def disableCursor(self):
        self.uart.write("CS0")

    def enableCursor(self):
        self.uart.write("CS1")

    def clear(self):
        self.uart.write("CL")

    def displayConfig(self, v):
        self.uart.write("DC", v)

    def rotate0(self):
        self.uart.write("SD0")

    def rotate90(self):
        self.uart.write("SD1")

    def rotate180(self):
        self.uart.write("SD2")

    def rotate270(self):
        self.uart.write("SD3")

    def print(self, s):
        self.uart.write("TT")
        self.uart.write(s)
        self.uart.write("\x00")

    def println(self, s):
        self.uart.write("TT")
        self.uart.write(s)
        self.uart.write("\x00")
        self.uart.write("TRT")
        
    def drawLine(self, x, y, x1, y1):
        self.uart.write("LN")
        self.write2B(x)
        self.write2B(y)
        self.write2B(x1)
        self.write2B(y1)

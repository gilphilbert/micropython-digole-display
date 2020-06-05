#Micropython driver for Digole Smart TFT
A Micropython driver for the Digole set of "smart" TFTs that can use UART (serial), I2C or SPI. They ship with UART by default - this library currently only supports serial mode.

Notes:
* Tested on an ESP8266 NodeMCU v3 board
* Should work with any Micropython board, just make sure you select the correct serial (and wire the display to the correct pins)
* Currently not much works, you can write text, change the brightness and draw lines but there's more coming...

## Configuration (NodeMCU v3)
Connect VCC / GND to 3v and GND of NodeMCU v3
Connect RX port of Digole display to D4 on the NodeMCU v3

##
I use ampy, do whatever feels natural:
```
ampy put digole_display.py
```

Now import:
```
from digole_display import DigoleDisplay
```
To use the defaults (serial 1, 9600) just instatiate:
```
dd = DigoleDisplay()
```
To change the baud rate or switch to serial 2, select:
```
dd = DigoleDisplay(serial=2, baud=115200)
```
Now start writing text:
```
dd.println("Hello!")
```

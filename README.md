#Wemos D1 Piano Example with MicroPython

###Flashing MicroPython
First step is to flash MicroPython firmware. The firmware can be downloaded from [here](http://micropython.org/download#esp8266).

To flash the fimware you need execture command:
```bash
esptool.py -p /dev/ttyUSB0 write_flash -fm dio -fs 32m -ff 40m 0x00000 esp8266-20161017-v1.8.5.bin
```
More information is available [here](https://docs.micropython.org/en/latest/esp8266/esp8266/tutorial/intro.html).


###Setup the software:

- Connect the board to the same network your computer is connected to:
https://docs.micropython.org/en/latest/esp8266/esp8266/tutorial/intro.html#wifi

- Connect to the board via webrepl (minimum once):
https://docs.micropython.org/en/latest/esp8266/esp8266/tutorial/repl.html#webrepl-a-prompt-over-wifi

- Download webrepl and upload the files ( [html.py](https://raw.githubusercontent.com/themperek/piano/master/html.py) and [main.py](https://raw.githubusercontent.com/themperek/piano/master/main.py) ) to the board:
http://micropython-on-wemos-d1-mini.readthedocs.io/en/latest/basics.html#uploading-files

###Running:
Go to: http://192.168.4.1

To get piano working connect beeper like described [here](http://micropython-on-wemos-d1-mini.readthedocs.io/en/latest/basics.html#beepers).

###Help in general can be found here:
http://micropython-on-wemos-d1-mini.readthedocs.io/en/latest/index.html
https://docs.micropython.org/en/latest/esp8266/index.html

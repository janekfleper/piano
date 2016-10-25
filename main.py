import html
import socket, os, gc
from machine import Pin, PWM

notes = {
    'c': 262,
    'd': 294,
    'e': 330,
    'f': 349,
    'g': 392,
    'a': 440,
    'b': 494,
    'C': 523,
    '0': 0,
}

# frequency needs to be set to 1 as PWM(freq) seems to be the same for all
# pins as mentioned in main()
def toggle_led(led):
    if (led.duty() == 1023):
        led.duty(511)
        led.freq(1)
        return 'on'
    else:
        led.duty(1023)
        return 'off'

def play_note(freq, beeper):
    if (freq == '0'):
        beeper.duty(0)
        return 0
    else:
        beeper.duty(511)
        beeper.freq(notes[freq])
        return notes[freq]

def get_frequency(parts, led, beeper):
    if (len(parts) < 2):
        return -1
    if (parts[0] != 'GET'):
        return -2
    if ('=' not in parts[1]):
        return -3

    print(parts)
    freq = parts[1].split('=')[-1]
    if (freq == ''):
        return -4
    print('frequency:', freq)

    if (freq == 'led'):
        print('led:', toggle_led(led))
    else:
        print('freq:', play_note(freq, beeper))

    return 0

def message(html):
    return """HTTP/1.0 200 OK
            Content-Type: text/html

            """ + html.get_html()

def main():
    addr = socket.getaddrinfo('0.0.0.0', 80)[0][-1]
    s = socket.socket()

    try:
        s.bind(addr)
    except OSError:
        machine.reset()

    s.listen(8)

# the beeper and the led appear to share a frequency...
    led = PWM(Pin(2), freq = 1, duty = 1023)
    beeper = PWM(Pin(14), freq = 0, duty = 0)

    while True:
        try:
            cl_conn, cl_addr = s.accept()
            recv = cl_conn.recv(4096)
            parts = recv.decode('ascii').split(' ')
            get_frequency(parts, led, beeper)

            cl_conn.sendall(message(html))
            cl_conn.close()
        except OSError:
            pass

main()

import pyfirmata
import time 
board = pyfirmata.Arduino('COM3')

while True:
    for i in range (5,11):
        board.digital[i].write(1)
        time.sleep(.3)
        board.digital[i].write(0)
        time.sleep(0)
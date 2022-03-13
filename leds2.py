
import pyfirmata
import time 
board = pyfirmata.Arduino('COM3')
import random as random

while True:
    led = random.randint(5,10)
    board.digital[led].write(1)
    time .sleep(3)
    board.digital[led].write(0)
    time.sleep(0)
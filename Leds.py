
import pyfirmata
import time 
board = pyfirmata.Arduino('COM3')

while True:
    #ROJOS
    board.digital[4].write(1)
    board.digital[8].write(1)
    time.sleep(.5)
    board.digital[4].write(0)
    board.digital[8].write(0)

    #AMARILLOS
    board.digital[6].write(1)
    board.digital[9].write(1)
    time.sleep(.5)
    board.digital[6].write(0)
    board.digital[9].write(0)
    

    #VERDES
    board.digital[7].write(1)
    board.digital[10].write(1)
    time.sleep(.5)
    board.digital[7].write(0)
    board.digital[10].write(0)
    
 
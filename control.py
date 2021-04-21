import RPi.GPIO as GPIO
import curses

GPIO.setwarnings(False)
screen = curses.initscr()
curses.noecho()
curses.cbreak()
screen.keypad(True)

GPIO.setmode(GPIO.BOARD)
GPIO.setup(33,GPIO.OUT)
GPIO.setup(11,GPIO.OUT)

GPIO.setup(13,GPIO.OUT)
GPIO.setup(15,GPIO.OUT)

GPIO.setup(29,GPIO.OUT)
GPIO.setup(31,GPIO.OUT)

GPIO.output(29,True)
GPIO.output(31,True)
try:
    while True:
        char = screen.getch()
        if char == ord('q'):
            break
        elif char == curses.KEY_UP:
            print("up")
            GPIO.output(33,True)
            GPIO.output(11,False)
            GPIO.output(13,True)
            GPIO.output(15,False)

        elif char == curses.KEY_DOWN:
            print("down")
            GPIO.output(33,False)
            GPIO.output(11,True)
            GPIO.output(13,False)
            GPIO.output(15,True)

        elif char == curses.KEY_RIGHT:
            print("right")
            GPIO.output(33,True)
            GPIO.output(11,False)
            GPIO.output(13,False)
            GPIO.output(15,True)

        elif char == curses.KEY_LEFT:
            print("left")
            GPIO.output(33,False)
            GPIO.output(11,True)
            GPIO.output(13,True)
            GPIO.output(15,False)
        elif char == 10:
            print("stop")
            GPIO.output(33,False)
            GPIO.output(11,False)
            GPIO.output(13,False)
            GPIO.output(15,False)
finally:
    curses.nocbreak()
    screen.keypad(0)
    curses.echo()
    curses.endwin()

from gpiozero import LED
from time import sleep

led = LED(25)

def morse(n):
    if(n == 0):
       for i in range (5):
            led.on()
            print("_")
            sleep(2)
            led.off()
            print(" ")
            sleep(0.2)    
    elif(n<=5):
        for i in range (n):
            led.on()
            print(".")
            sleep(0.5)
            led.off()
            print(" ")
            sleep(0.2)          
        for i in range (5-n):
            led.on()
            print("_")
            sleep(2)
            led.off()
            print(" ")
            sleep(0.2) 
    else:      
        for i in range (n-5):
            led.on()
            print("_")
            sleep(2)
            led.off()
            print(" ")
            sleep(0.2)
        for i in range (10-n):
            led.on()
            print(".")
            sleep(0.5)
            led.off()
            print(" ")
            sleep(0.2) 

num = int(input())
morse(num)

#from gpiozero import LED
from time import sleep

#led = LED(25)

def morse(n):
    if(n == 0):
       for i in range (5):
            led.on()
            print(".")
            sleep(1)
            led.off()
            print(" ")
            sleep(0.3)    
    elif(n<=5):
        for i in range (n):
            led.on()
            print(".")
            sleep(1)
            led.off()
            print(" ")
            sleep(0.3)          
        for i in range (5-n):
            led.off()
            print(" ")
            sleep(1)
            led.off()
            print(" ")
            sleep(0.3) 
    else:      
        for i in range (n-5):
            led.off()
            print(" ")
            sleep(1)
            led.off()
            print(" ")
            sleep(0.3)
        for i in range (10-n):
            led.on()
            print(".")
            sleep(1)
            led.off()
            print(" ")
            sleep(0.3) 

num = int(input())
morse(num)
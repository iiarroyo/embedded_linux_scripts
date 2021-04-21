from gpiozero import LED
from time import sleep
from gpiozero import Button
led = LED(25) #led pin 25
button = Button(2) # boton pin 2
while True:
    try: 
        button.wait_for_press()# esperar presionado
        #prender led despues de presionado
        led.on() 
        sleep(3)
        led.off()
    except KeyboardInterrupt:
        print("Programa finalizado")
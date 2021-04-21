from gpiozero import LED
from time import sleep
from gpiozero import Button
button = Button(2) # boton pin 2
while True:
    button.wait_for_press()# esperar presionado
    #prender led despues de presionado
    print("Botón presionado")

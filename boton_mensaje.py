from gpiozero import LED
from time import sleep
from gpiozero import Button
led = LED(25) #led pin 25
button = Button(2) # boton pin 2
bandera = True
while bandera: #ejecuta instruccion hasta interrupcion
    try:
        button.wait_for_press()# esperar presionado
        #prender led despues de presionado
        #imprimir mensaje en consola
        print("Botón presionado")
        led.on() 
        led.off()
    except KeyboardInterrupt:
        print("Programa finalizado")
        bandera = False
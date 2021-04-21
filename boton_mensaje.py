from gpiozero import LED
from time import sleep
from gpiozero import Button
led = LED(25) #led pin 25
button = Button(2) # boton pin 2
bandera = True
while bandera: #ejecuta instruccion hasta interrupcion
    try:
        button.wait_for_press()# esperar presionado
        print("Botón presionado") 
        led.on()
        #prender led despues de presionado
        #imprimir mensaje en consola

        button.wait_for_release()# esperar presionado
        led.off()
    except KeyboardInterrupt:
        print("Programa finalizado")
        bandera = False
#Blinking LED script

#libreria para manipulacion de GIPIO
from gpiozero import LED
#libreria para temporizador
from time import sleep
#asignacion del pin 25 al led
led = LED(25)
# Ciclo para ejecutar desde el encendido a apaque
while True:
    #encender el led
    led.on()
    #esperar un segundo
    sleep(1)
    #apagar led
    led.off()
    #esperar un segundo
    sleep(1)
    #print ("listo")

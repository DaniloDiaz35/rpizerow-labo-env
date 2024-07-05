from gpiozero import LED, Buzzer
from signal import pause

buzzer = Buzzer(22)
led_r = LED(19)
led_g = LED(26)
led_b = LED(13)
while True:
	comando = input("Ingrese lo que quiere activar:  buzzer o colores: ")
	if comando == "colores":
		opcion = input("Ingrese opcion: r(rojo), g(green) or b(blue): ")
	elif comando == "buzzer":
		opcion = input("Ingrese opcion: on u off: ")		

	if comando == "buzzer":
		if opcion == "on":
			buzzer.on()
		elif opcion == "off":
			buzzer.off()

	elif comando == "colores":
		if opcion == "r":
			led_r.toggle()
		elif opcion == "g":
			led_g.toggle()
		elif opcion == "b":
			led_b.toggle()			

pause()

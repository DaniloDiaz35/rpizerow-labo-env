import gpiozero
import Adafruit_ADS1x15

adc = Adafruit_ADS1x15.ADS1115()

led_r = PWMLED(17)
led_b = PWMLED(27)

Resistencia_Ref = 10000.0
Beta_Term = 3900.0 

GAIN_act = 1

def main():
	while True:
        	temp_setpoint = read_potentiometer()
        	actual_temp = read_thermistor()
        	control_leds(temp_setpoint, actual_temp)
        	print(f"Setpoint: {temp_setpoint:.2f}°C, Actual: {actual_temp:.2f}°C")
        	time.sleep(1)

def read_potentiometer():
    	value = adc.read_adc(0, gain=GAIN_act)
    	temperature_setpoint = value * 30.0 / 32767.0
    	return temperature_setpoint

def read_thermistor():
	value = adc.read_adc(1, gain=GAIN_act)
	resistencia = Resistencia_Ref * (32767.0 / value - 1.0)
	temperature = 1.0 / (1.0 / 298.15 + (1.0 / Beta_Term) * (resistencia / Resistencia_Ref - 1.0)) - 273.15
	return temperature

def control_leds(temp_setpoint, actual_temp):
	difference = actual_temp - temp_setpoint
	max_difference = 5.0
	duty_cycle = min(abs(difference) / max_difference, 1.0)

	if difference > 0:
		led_b.value = duty_cycle
        	led_r.value = 0
    	else:
        	led_r.value = duty_cycle
        	led_b.value = 0


if _name_ == "_main_":
	main()

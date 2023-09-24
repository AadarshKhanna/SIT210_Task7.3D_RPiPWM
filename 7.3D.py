from time import sleep
from gpiozero import DistanceSensor, PWMLED                          # Importing necessary modules

# Initializing an LED on GPIO pin 18
led = PWMLED(18)
distance_sensor = DistanceSensor(echo=14, trigger=15)                # Initializing a distance sensor on GPIO pins 14 (echo) and 15 (trigger)

#main function
def main():
    try:
        led.on()        # First turning the LED on
        
        # Continuously reading distance measurements
        while True:
            distance_cm = distance_sensor.value * 100
            print(f'Distance: {distance_cm:1.2f} CM')

            led_distance = distance_sensor.value
            brightness = round(1.0 - led_distance * 3, 1)            # Calculating LED brightness based on distance

            # Ensuring brightness is always postive
            if brightness < 0:
                brightness = 0.0

            led.value = brightness            # Setting the LED brightness
            sleep(0.1)
    
    except KeyboardInterrupt:
        pass
    
    finally:
        led.off()        # Turning the LED off and closing the distance sensor
        distance_sensor.close()

main()# Calling the main function to start execution
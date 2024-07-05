import Adafruit_DHT
import time

# Defina o tipo de sensor e o pino de dados
SENSOR = Adafruit_DHT.DHT11
PIN = 4

def read_air_quality():
    humidity, temperature = Adafruit_DHT.read(SENSOR, PIN)
    if humidity is not None and temperature is not None:
        return {'temperature': temperature, 'humidity': humidity}
    else:
        return None

while True:
    data = read_air_quality()
    if data:
        print(f"Temp: {data['temperature']}C Humidity: {data['humidity']}%")
    else:
        print("Failed to get reading. Try again!")
    time.sleep(2)

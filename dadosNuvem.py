import time
import json
import Adafruit_DHT
import paho.mqtt.client as mqtt

# Configurações do sensor
SENSOR = Adafruit_DHT.DHT11
PIN = 4

# Configurações do AWS IoT Core
AWS_ENDPOINT = "seu-endpoint.iot.us-east-1.amazonaws.com"
CLIENT_ID = "RaspberryPi"
TOPIC = "air_quality/data"
CERT_PATH = "/caminho/para/certificado.pem.crt"
KEY_PATH = "/caminho/para/private.pem.key"
ROOT_CA = "/caminho/para/AmazonRootCA1.pem"

# Função de callback para conexão
def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {rc}")

# Função para coletar dados do sensor
def read_air_quality():
    humidity, temperature = Adafruit_DHT.read(SENSOR, PIN)
    if humidity is not None and temperature is not None:
        return {'temperature': temperature, 'humidity': humidity}
    else:
        return None

# Configuração do cliente MQTT
client = mqtt.Client(CLIENT_ID)
client.tls_set(ROOT_CA, certfile=CERT_PATH, keyfile=KEY_PATH)
client.on_connect = on_connect
client.connect(AWS_ENDPOINT, 8883, 60)

client.loop_start()

while True:
    data = read_air_quality()
    if data:
        payload = json.dumps(data)
        client.publish(TOPIC, payload)
        print(f"Published: {payload}")
    else:
        print("Failed to get reading. Try again!")
    time.sleep(5)

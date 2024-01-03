import network
import time
from umqtt.simple import MQTTClient
from machine import Pin, I2C

# import micropython lib for sensor
import TSL2591


# Function to load configuration
def load_config(filename='config.txt'):
    config = {}
    with open(filename, 'r') as file:
        for line in file:
            if '=' in line:
                key, value = line.strip().split('=', 1)
                config[key] = value
    return config


# Load the configuration
config = load_config()

# WiFi and MQTT Configuration
wifi_ssid = config.get('WIFI_SSID')
wifi_password = config.get('WIFI_PASSWORD')
mqtt_host = config.get('MQTT_HOST')
mqtt_username = config.get('MQTT_USERNAME')
mqtt_password = config.get('MQTT_PASSWORD')
mqtt_publish_topic = config.get('MQTT_PUBLISH_TOPIC')
mqtt_client_id = config.get('MQTT_CLIENT_ID')
mqtt_subscribe_topic = config.get('MQTT_PUBLISH_TOPIC')
mqtt_subscribe_topic2 = config.get('MQTT_PUBLISH_TOPIC2')

# Connect to WiFi
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(wifi_ssid, wifi_password)
while not wlan.isconnected():
    print('Waiting for connection...')
    time.sleep(1)
print("Connected to WiFi")


# Initialize MQTT client and set message callback
def on_message(topic, msg):
    print(f"Received message '{msg}' on topic '{topic}'")
    if msg == b'1':
        red.value(1)
    elif msg == b'0':
        red.value(0)

mqtt_client = MQTTClient(client_id=mqtt_client_id, server=mqtt_host,
                         user=mqtt_username, password=mqtt_password)
mqtt_client.set_callback(on_message)
mqtt_client.connect()
mqtt_client.subscribe(mqtt_subscribe_topic)  # Subscribe to the topic
mqtt_client.subscribe(mqtt_subscribe_topic2)

# LED and Button setup
red = Pin('GP10', Pin.OUT)

# sensor variables

sdaPIN=machine.Pin(0)
sclPIN=machine.Pin(1)
i2c_bus = 0
addr = 0x29

i2c=machine.I2C(i2c_bus, sda=sdaPIN, scl=sclPIN, freq=400000)

tsl = TSL2591.TSL2591(i2c, addr)

# Variables for button debounce
wait_time = 0

try:
    while True:
        mqtt_client.check_msg()  # Check for new messages and call on_message

        if time.ticks_ms() - wait_time > 10000:  # Wait time check
            lux = tsl.lux
            print("Lux: {}  ".format(lux))     

            wait_time = time.ticks_ms()

            mqtt_client.publish(mqtt_publish_topic, str(lux))

except KeyboardInterrupt:
    red.value(0)  # Ensure the LED is turned off
    print("Application stopped.")
finally:
    mqtt_client.disconnect()

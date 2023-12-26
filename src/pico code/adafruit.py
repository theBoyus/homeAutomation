import network
import time
from machine import Pin
from umqtt.simple import MQTTClient
from math import sin


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

# LED and Button setup
red = Pin('GP15', Pin.OUT)
button = Pin(18, Pin.IN, Pin.PULL_UP)

# Variables for button debounce
debounce_time = 0

try:
    while True:
        mqtt_client.check_msg()  # Check for new messages and call on_message

        # Check for button press
        if button.value() == 0 and time.ticks_ms() - debounce_time > 500:  # Debounce check
            print("Button pressed")
            debounce_time = time.ticks_ms()

            # Publish a message to the MQTT server
            sine = sin(time.ticks_ms() / 1000)  # Generate dummy data
            print(f'Publish {sine:.2f}')
            mqtt_client.publish(mqtt_publish_topic, str(sine))

except KeyboardInterrupt:
    red.value(0)  # Ensure the LED is turned off
    print("Application stopped.")
finally:
    mqtt_client.disconnect()

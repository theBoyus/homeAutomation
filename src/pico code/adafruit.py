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

# Connect to WiFi
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(wifi_ssid, wifi_password)
while not wlan.isconnected():
    print('Waiting for connection...')
    time.sleep(1)
print("Connected to WiFi")

# Initialize MQTT client
mqtt_client = MQTTClient(client_id=mqtt_client_id, server=mqtt_host,
                         user=mqtt_username, password=mqtt_password)
mqtt_client.connect()

# LED and Button setup
red = Pin('GP15', Pin.OUT)
button = Pin(18, Pin.IN, Pin.PULL_UP)

# Variables for LED blinking and button debounce
last_toggle_time = 0
toggle_interval = 1  # Change LED state every 1 second
debounce_time = 0

try:
    while True:
        current_time = time.ticks_ms()

        # Toggle the LED every 1 second
        if current_time - last_toggle_time > toggle_interval * 1000:
            red.value(not red.value())
            last_toggle_time = current_time

        # Check for button press
        if button.value() == 0 and current_time - debounce_time > 500:  # Debounce check
            print("Button pressed")
            debounce_time = current_time

            # Publish a message to the MQTT server
            sine = sin(time.ticks_ms() / 1000)  # Generate dummy data
            print(f'Publish {sine:.2f}')
            mqtt_client.publish(mqtt_publish_topic, str(sine))

except KeyboardInterrupt:
    red.value(0)  # Ensure the LED is turned off
    print("Application stopped.")
finally:
    mqtt_client.disconnect()

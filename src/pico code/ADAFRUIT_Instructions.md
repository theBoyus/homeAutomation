
# Running adafruit.py on Raspberry Pi Pico

To successfully run the `adafruit.py` script on your Raspberry Pi Pico, you'll need to create a configuration file named `config.txt` and save it on the Pi Pico. This file should contain several key pieces of information that the script uses to connect to Adafruit IO and your WiFi network.

## Configuration File Format

Your `config.txt` file should include the following information:

```
WIFI_SSID=<Your WiFi SSID>
WIFI_PASSWORD=<Your WiFi Password>
MQTT_HOST=io.adafruit.com
MQTT_USERNAME=<Your Adafruit Username>
MQTT_PASSWORD=<Your Adafruit IO Key>
MQTT_PUBLISH_TOPIC=<Your Adafruit Publish Topic>
MQTT_CLIENT_ID=<A Unique Client ID>
```

Replace the placeholder text (e.g., `<Your WiFi SSID>`) with your actual information. Here's what each line in `config.txt` represents:

- `WIFI_SSID`: Your WiFi network name.
- `WIFI_PASSWORD`: Your WiFi network password.
- `MQTT_HOST`: The server for Adafruit IO. Default is `io.adafruit.com` (use as-is for Adafruit IO).
- `MQTT_USERNAME`: Your username as registered on Adafruit IO.
- `MQTT_PASSWORD`: Your Adafruit IO Key (found in your Adafruit IO account settings).
- `MQTT_PUBLISH_TOPIC`: The topic to which you'll be publishing data. Format it as `username/feeds/feedname` (no quotes needed).
- `MQTT_CLIENT_ID`: A unique identifier for your device. It should be unique to avoid conflicts with other users.

### Example `config.txt`

```
WIFI_SSID=myWifiNetwork
WIFI_PASSWORD=myWifiPassword
MQTT_HOST=io.adafruit.com
MQTT_USERNAME=johndoe
MQTT_PASSWORD=aio_testKey12345
MQTT_PUBLISH_TOPIC=johndoe/feeds/myfeed
MQTT_CLIENT_ID=myPicoDevice01
```

## Instructions for Use

1. Create a text file named `config.txt`.
2. Fill in the necessary details as per the format provided above.
3. Save this file onto your Raspberry Pi Pico.
4. Run the `adafruit.py` script on your Pi Pico.

Note: Ensure that there are no spaces before or after the "=" in your `config.txt` file.

By following these instructions, your Raspberry Pi Pico should be able to connect to your WiFi network and Adafruit IO, allowing it to publish data to the specified feed.

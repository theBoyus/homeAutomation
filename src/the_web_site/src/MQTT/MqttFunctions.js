import { useState, useCallback, useContext } from "react";
import axios from "axios";
import { useAuth } from "../firebase/useAuth";

const MqttFunctions = (feed) => {
  const { mqttCredentials } = useAuth();
  const AIO_USERNAME = mqttCredentials?.mqtt_username;
  const AIO_KEY = mqttCredentials?.mqtt_password;
  const API_BASE_URL = "https://io.adafruit.com/api/v2";
  const FEED_KEY = feed; // Change this to your feed name

  const [latestData, setLatestData] = useState("");

  const fetchLatestFeedData = useCallback(() => {
    if (!AIO_USERNAME || !AIO_KEY) {
      console.error("MQTT credentials are not available.");
      return;
    }

    axios
      .get(`${API_BASE_URL}/${AIO_USERNAME}/feeds/${FEED_KEY}/data?limit=1`, {
        headers: { "X-AIO-Key": AIO_KEY },
      })
      .then((response) => {
        setLatestData(response.data[0].value);
      })
      .catch((error) => {
        console.error("Error fetching data:", error);
      });
  }, [AIO_USERNAME, AIO_KEY]);

  const sendDataToFeed = useCallback(
    (value) => {
      if (!AIO_USERNAME || !AIO_KEY) {
        console.error("Cannot send data: MQTT credentials are not available.");
        return;
      }

      const data = { value: value };
      axios
        .post(`${API_BASE_URL}/${AIO_USERNAME}/feeds/${FEED_KEY}/data`, data, {
          headers: { "X-AIO-Key": AIO_KEY },
        })
        .then((response) => {
          console.log(`Data ${value} sent:`, response.data);
          fetchLatestFeedData();
        })
        .catch((error) => {
          console.error(`Error sending data ${value}:`, error);
        });
    },
    [AIO_USERNAME, AIO_KEY, fetchLatestFeedData]
  );

  return { latestData, fetchLatestFeedData, sendDataToFeed };
};

export default MqttFunctions;

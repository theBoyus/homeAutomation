import { useState, useCallback, useContext } from "react";
import axios from "axios";
import { useAuth } from "../firebase/useAuth";

const MqttFunctions = () => {
  const { mqttCredentials } = useAuth();
  const AIO_USERNAME = mqttCredentials?.mqtt_username;
  const AIO_KEY = mqttCredentials?.mqtt_password;
  const API_BASE_URL = "https://io.adafruit.com/api/v2";

  const [latestData, setLatestData] = useState("");

  const fetchLatestFeedData = useCallback(
    (feed) => {
      if (!AIO_USERNAME || !AIO_KEY) {
        console.error("MQTT credentials are not available.");
        return Promise.reject("MQTT credentials not available");
      }

      return axios
        .get(`${API_BASE_URL}/${AIO_USERNAME}/feeds/${feed}/data?limit=1`, {
          headers: { "X-AIO-Key": AIO_KEY },
        })
        .then((response) => {
          setLatestData(response.data[0].value);
          return response.data[0].value; // Return the fetched value
        })
        .catch((error) => {
          console.error("Error fetching data:", error);
          return Promise.reject(error); // Reject the promise in case of error
        });
    },
    [AIO_USERNAME, AIO_KEY]
  );

  const sendDataToFeed = useCallback(
    (value, feed) => {
      if (!AIO_USERNAME || !AIO_KEY) {
        console.error("Cannot send data: MQTT credentials are not available.");
        return;
      }

      const data = { value: value };
      axios
        .post(`${API_BASE_URL}/${AIO_USERNAME}/feeds/${feed}/data`, data, {
          headers: { "X-AIO-Key": AIO_KEY },
        })
        .then((response) => {
          console.log(`Data ${value} sent to ${feed}:`, response.data);
          fetchLatestFeedData(feed);
        })
        .catch((error) => {
          console.error(`Error sending data ${value} to ${feed}:`, error);
        });
    },
    [AIO_USERNAME, AIO_KEY, fetchLatestFeedData]
  );

  return { latestData, fetchLatestFeedData, sendDataToFeed };
};

export default MqttFunctions;

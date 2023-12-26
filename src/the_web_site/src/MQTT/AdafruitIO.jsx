import React, { useState, useEffect } from "react";
import axios from "axios";
import { useAuth } from "../firebase/useAuth";

const AdafruitIO = () => {
  const { mqttCredentials } = useAuth();
  const AIO_USERNAME = mqttCredentials?.mqtt_username;
  const AIO_KEY = mqttCredentials?.mqtt_password;
  const API_BASE_URL = "https://io.adafruit.com/api/v2";
  const FEED_KEY = "data"; // Change this if you have another feed name

  const [latestData, setLatestData] = useState("");

  const fetchLatestFeedData = () => {
    if (!AIO_USERNAME || !AIO_KEY) {
      console.log("MQTT credentials are not available yet.");
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
  };

  useEffect(() => {
    fetchLatestFeedData();
  }, [AIO_USERNAME, AIO_KEY]);

  const sendDataToFeed = (value) => {
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
  };

  return (
    <div>
      <button onClick={() => sendDataToFeed("1")}>Send 1</button>
      <button onClick={() => sendDataToFeed("0")}>Send 0</button>
      <button onClick={fetchLatestFeedData}>Fetch Data</button>
      <div>Latest Data: {latestData}</div>
    </div>
  );
};

export default AdafruitIO;

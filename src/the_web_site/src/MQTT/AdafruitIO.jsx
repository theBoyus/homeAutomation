import React, { useState, useEffect } from 'react';
import axios from 'axios';

const AdafruitIO = () => {
  const AIO_USERNAME = process.env.REACT_APP_MQTT_USERNAME;
  const AIO_KEY = process.env.REACT_APP_MQTT_PASSWORD;
  const API_BASE_URL = 'https://io.adafruit.com/api/v2';
  const FEED_KEY = 'data'; // change this if you have other feed name

  const [latestData, setLatestData] = useState('');

  const sendDataToFeed = (value) => {
    const data = { value: value };

    axios.post(`${API_BASE_URL}/${AIO_USERNAME}/feeds/${FEED_KEY}/data`, data, {
      headers: { 'X-AIO-Key': AIO_KEY }
    })
    .then(response => {
      console.log(`Data ${value} sent:`, response.data);
      fetchLatestFeedData();
    })
    .catch(error => {
      console.error(`Error sending data ${value}:`, error);
    });
  };

  const fetchLatestFeedData = () => {
    axios.get(`${API_BASE_URL}/${AIO_USERNAME}/feeds/${FEED_KEY}/data?limit=1`, {
      headers: { 'X-AIO-Key': AIO_KEY }
    })
    .then(response => {
      setLatestData(response.data[0].value);
      console.log(response.data[0])
    })
    .catch(error => {
      console.error('Error fetching data:', error);
    });
  };

  useEffect(() => {
    const interval = setInterval(() => {
      fetchLatestFeedData();
    }, 20000);

    return () => clearInterval(interval);
  }, []);

  return (
    <div>
      <button onClick={() => sendDataToFeed("1")}>Send 1</button>
      <button onClick={() => sendDataToFeed("0")}>Send 0</button>
      <div>
        Latest Data: {latestData}
      </div>
    </div>
  );
};

export default AdafruitIO;

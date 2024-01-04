import { useState, useEffect } from "react";
import MqttFunctions from "../../../MQTT/MqttFunctions";
import "../../css/LightSwitch.css";
import { DNA } from "react-loader-spinner";

const LightSwitch = () => {
  const { latestData, fetchLatestFeedData, sendDataToFeed } =
    MqttFunctions("lightswitch");
  const [isChecked, setIsChecked] = useState(false);

  useEffect(() => {
    fetchLatestFeedData();
  }, [fetchLatestFeedData]);

  useEffect(() => {
    setIsChecked(latestData === "1");
  }, [latestData]);

  const handleOnChange = () => {
    const newCheckedState = !isChecked;
    setIsChecked(newCheckedState);
    sendDataToFeed(newCheckedState ? "1" : "0");
  };

  return (
    <div className="container">
      {latestData ? (
        <div>
          <input
            className="toggleLight"
            type="checkbox"
            checked={isChecked}
            onChange={handleOnChange}
          />
        </div>
      ) : (
        <DNA />
      )}
    </div>
  );
};

export default LightSwitch;

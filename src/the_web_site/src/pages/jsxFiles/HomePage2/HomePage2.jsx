import { useState } from "react";
import LightSwitch from "./LightSwitch";
import "../../css/HomePage2.css";
import Schedule from "./Schedule";

const HomePage2 = () => {
  const [activeElement, setActiveElement] = useState(null);

  const showElement = (elementId) => {
    setActiveElement(elementId);
  };

  return (
    <div className="mainContainer">
      <div className="optionsContainer">
        <button
          className="optionsButton"
          onClick={() => showElement("lightSwitch")}
        >
          Light Switch
        </button>
        <button
          className="optionsButton"
          onClick={() => showElement("schedule")}
        >
          Schedule
        </button>
        <button
          className="optionsButton"
          onClick={() => showElement("lightBased")}
        >
          Light-based
        </button>
        <button
          className="optionsButton"
          onClick={() => showElement("systemControl")}
        >
          System control
        </button>
      </div>
      <div className="activeElementContainer">
        {activeElement === null && (
          <div className="welcomeMessage">
            Welcome! Please select an option.
          </div>
        )}
        {activeElement === "lightSwitch" && <LightSwitch />}
        {activeElement === "schedule" && <Schedule />}
      </div>
    </div>
  );
};

export default HomePage2;

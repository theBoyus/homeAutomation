import React, { useState } from "react";
import TimePicker from "react-time-picker";
import "../css/HomePage.css";

function HomePage() {
  const options = [
    "Manual Switch",
    "Schedule",
    "Light-based",
    "System control",
  ];
  const [selectedOption, setSelectedOption] = useState(null);
  const [startTime, setStartTime] = useState("12:00");
  const [endTime, setEndTime] = useState("12:00");

  const handleOptionChange = (option) => {
    setSelectedOption(option);
  };

  const handleButtonClick = (action) => {
    console.log(`Button ${action} clicked`);
    // Add your logic here for button actions
  };

  const handleApplySettings = () => {
    console.log("Settings applied:", { startTime, endTime });
    // Add logic to apply settings
  };

  const handleResetTimers = () => {
    setStartTime("00:00");
    setEndTime("00:00");
  };

  return (
    <div className="homepage-container">
      {/* Options Box */}
      <div className="options-container">
        {options.map((option) => (
          <label key={option} className="option-label">
            <input
              type="radio"
              value={option}
              checked={selectedOption === option}
              onChange={() => handleOptionChange(option)}
            />
            {option.charAt(0).toUpperCase() + option.slice(1)}{" "}
          </label>
        ))}
      </div>

      {/* Right Box */}
      <div className="right-box">
        {selectedOption === "Manual Switch" && (
          <div>
            <button
              onClick={() => handleButtonClick("On")}
              className="homepage-button"
            >
              On
            </button>
            <button
              onClick={() => handleButtonClick("Off")}
              className="homepage-button"
            >
              Off
            </button>
            <p>Turns the LED On or OFF</p>
          </div>
        )}

        {selectedOption === "Schedule" && (
          <div>
            <label>Start Time:</label>
            <input
              type="time"
              value={startTime}
              onChange={(e) => setStartTime(e.target.value)}
              className="homepage-button"
            />
            <br />
            <label>End Time:</label>
            <input
              type="time"
              value={endTime}
              onChange={(e) => setEndTime(e.target.value)}
              className="homepage-button"
            />
            <br />
            <button onClick={handleApplySettings} className="homepage-button">
              Apply Settings
            </button>
            <button onClick={handleResetTimers} className="homepage-button">
              Reset Timers
            </button>
            <p>Set a timer for the device.</p>
          </div>
        )}

        {selectedOption === "Light-based" && (
          <div>
            <img
              src="https://via.placeholder.com/100"
              alt="Blank 100px by 100px image"
              style={{ width: "100px", height: "100px" }}
            />
            <button
              onClick={() => handleButtonClick("Option3")}
              className="homepage-button"
            >
              Click me
            </button>
            <p>
              Here we'll have 1 dropdown (Select light sensitivity) and 2
              buttons to toggle mode and maybe an image of light data history?
            </p>
          </div>
        )}

        {selectedOption === "System control" && (
          <div>
            <button
              onClick={() => handleButtonClick("Shut it down")}
              className="homepage-button"
            >
              Shut it down
            </button>
            <button
              onClick={() => handleButtonClick("Boot it up")}
              className="homepage-button"
            >
              Boot it up
            </button>
            <p>Control the device state.</p>
          </div>
        )}
      </div>
    </div>
  );
}

export default HomePage;

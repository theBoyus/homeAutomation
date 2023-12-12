// HomePage.js

import { useState } from "react";
import "../css/HomePage.css";

function HomePage() {
  const options = ["Manual Switch", "Schedule", "Light-based", "System control"];
  const [selectedOption, setSelectedOption] = useState(null);

  const handleOptionChange = (option) => {
    setSelectedOption(option);
  };

  const handleButtonClick = (action) => {
    console.log(`Button ${action} clicked`);
    // Add your logic here for button actions
  };

  const [starthour, setStarthour] = useState("");
  const [endhour, setEndhour] = useState("");

  const handlestartHourChange = (event) => {
    setStarthour(event.target.value);
  };

  const handleendHourChange = (event) => {
    setEndhour(event.target.value);
  };

  const generateHours = () => {
    return Array.from({ length: 24 }, (_, index) => index);
  };

  const contentMap = {
    option1: (
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
    ),
    option2: (
      <div>
        <label>Start Time:</label>
        <select
          className="homepage-button start"
          value={starthour}
          onChange={handlestartHourChange}
        >
          {generateHours().map((h) => (
            <option key={h} value={h}>
              {h < 10 ? `0${h}:00` : `${h}:00`}
            </option>
          ))}
        </select>
        <br />
        <label>End Time:</label>
        <select
          className="homepage-button end"
          value={endhour}
          onChange={handleendHourChange}
        >
          {generateHours().map((h) => (
            <option key={h} value={h}>
              {h < 10 ? `0${h}:00` : `${h}:00`}
            </option>
          ))}
        </select>
        <p>Set a timer for the device.</p>
      </div>
    ),
    option3: (
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
        <p>Display an image and a button.</p>
      </div>
    ),
    option4: (
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
        <p>Control the device power.</p>
      </div>
    ),
  };

  const content = contentMap[selectedOption] || "Select an option";

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
      <div className="right-box">{content}</div>
    </div>
  );
}

export default HomePage;

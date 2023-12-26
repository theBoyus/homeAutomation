import {useState} from "react";
import OptionContent from "./OptionContent";
import "../../css/HomePage.css";

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

  const handleOptionChange = (option) => setSelectedOption(option);

  const handleButtonClick = (action) => console.log(`Button ${action} clicked`);

  const handleApplySettings = () =>
    console.log("Settings applied:", { startTime, endTime });

  const handleResetTimers = () => {
    setStartTime("00:00");
    setEndTime("00:00");
  };

  

  return (
    <div className="homepage-container">
      <div className="options-container">
        {options.map((option) => (
          <label key={option} className="option-label">
            <input
              type="radio"
              value={option}
              checked={selectedOption === option}
              onChange={() => handleOptionChange(option)}
            />
            {option.charAt(0).toUpperCase() + option.slice(1)}
          </label>
        ))}
      </div>
      <div className="right-box">
        <OptionContent
          selectedOption={selectedOption}
          startTime={startTime}
          endTime={endTime}
          onTimeChange={setStartTime}
          onEndTimeChange={setEndTime}
          onApplySettings={handleApplySettings}
          onResetTimers={handleResetTimers}
          onButtonClick={handleButtonClick}
        />
      </div>
    </div>
  );
}



export default HomePage;

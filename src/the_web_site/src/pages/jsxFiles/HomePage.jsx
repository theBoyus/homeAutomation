import { useState } from "react";
import "../css/HomePage.css";

function HomePage() {
  const options = ["option1", "option2", "option3", "option4"];
  const [selectedOption, setSelectedOption] = useState(null);

  const handleOptionChange = (option) => {
    setSelectedOption(option);
  };

  const [starthour, setStarthour] = useState("");

  const [endhour, setEndhour] = useState("");

  const handlestartHourChange = (event) => {
    setStarthour(event.target.value);
  };

  const handleendHourChange = (event) => {
    setEndhour(event.target.value);
  };

  const hours = Array.from({ length: 24 }, (_, index) => index); // generate array from 0 to 23

  return (
    /*
        <div>
        Timer
        <select className="start" value={starthour} onChange={handlestartHourChange}>
        {hours.map((h) => (
            <option key={h} value={h}>
            {h < 10 ? `0${h}:00` : `${h}:00`} 
            </option>
        ))}
        </select>
        <select className="end" value={endhour} onChange={handleendHourChange}>
        {hours.map((h) => (
            <option key={h} value={h}>
            {h < 10 ? `0${h}:00` : `${h}:00`}
        ))}
        </select>
        </div>
        */
    <div>
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
            {/* Capitalize the first letter */}
          </label>
        ))}
      </div>

      <div className="right-box">
        <h2>Right Box Content</h2>
        <p>{content}</p>
      </div>
    </div>
  );
}

export default HomePage;

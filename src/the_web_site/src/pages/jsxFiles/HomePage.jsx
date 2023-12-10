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

  const contentMap = {
    option1: "Content for Option 1",
    option2: "Content for Option 2",
    option3: "Content for Option 3",
    option4: "Content for Option 4",
  };

  const handleendHourChange = (event) => {
    setEndhour(event.target.value);
  };

  const hours = Array.from({ length: 24 }, (_, index) => index); // generate array from 0 to 23

  const content = contentMap[selectedOption] || "Select an option";

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
    <div className="container">
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

      <div className="right-box">
        <p>{content}</p>
      </div>
    </div>
  );
}

export default HomePage;

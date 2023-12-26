const ManualSwitch = ({ onButtonClick }) => (
  <div>
    <button onClick={() => onButtonClick("On")} className="homepage-button">
      On
    </button>
    <button onClick={() => onButtonClick("Off")} className="homepage-button">
      Off
    </button>
    <p>Turns the LED On or OFF</p>
  </div>
);

const Schedule = ({
  startTime,
  endTime,
  onTimeChange,
  onEndTimeChange,
  onApplySettings,
  onResetTimers,
}) => (
  <div>
    <label>Start Time:</label>
    <input
      type="time"
      value={startTime}
      onChange={(e) => onTimeChange(e.target.value)}
      className="homepage-button"
    />
    <br />
    <label>End Time:</label>
    <input
      type="time"
      value={endTime}
      onChange={(e) => onEndTimeChange(e.target.value)}
      className="homepage-button"
    />
    <br />
    <button onClick={onApplySettings} className="homepage-button">
      Apply Settings
    </button>
    <button onClick={onResetTimers} className="homepage-button">
      Reset Timers
    </button>
    <p>Set a timer for the device.</p>
  </div>
);

const LightBased = ({ onButtonClick }) => (
  <div>
    <img
      src="https://via.placeholder.com/100"
      alt="Light Data"
      style={{ width: "100px", height: "100px" }}
    />
    <button
      onClick={() => onButtonClick("Option3")}
      className="homepage-button"
    >
      Click me
    </button>
    <p>Select light sensitivity and view light data history.</p>
  </div>
);

const SystemControl = ({ onButtonClick }) => (
  <div>
    <button
      onClick={() => onButtonClick("Shut it down")}
      className="homepage-button"
    >
      Shut it down
    </button>
    <button
      onClick={() => onButtonClick("Boot it up")}
      className="homepage-button"
    >
      Boot it up
    </button>
    <p>Control the device state.</p>
  </div>
);

export default { ManualSwitch, Schedule, LightBased, SystemControl };
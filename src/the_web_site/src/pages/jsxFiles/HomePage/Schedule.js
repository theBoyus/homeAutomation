import { useState, useEffect } from "react";
import { useData } from "../../DataContext";
import "../../css/Schedule.css";
import { Trash } from "react-bootstrap-icons";
import MqttFunctions from "../../../MQTT/MqttFunctions";

function Schedule() {
  const { data, updateData } = useData();
  const [scheduledMessages, setScheduledMessages] = useState([]);
  const [action, setAction] = useState("Turn On");

  // Initialize MQTT functions
   const { sendDataToFeed } = MqttFunctions();

  useEffect(() => {
    const storedMessages = JSON.parse(
      localStorage.getItem("scheduledMessages")
    );
    if (storedMessages) {
      setScheduledMessages(storedMessages);
    }
  }, []);

  useEffect(() => {
    const interval = setInterval(() => {
      setScheduledMessages((currentMessages) =>
        currentMessages.map((message) => ({
          ...message,
          timeLeft: calculateTimeLeft(message.time),
        }))
      );
    }, 1000);

    return () => clearInterval(interval);
  }, []);

  const calculateTimeLeft = (scheduledTime) => {
    const now = new Date();
    const [hours, minutes] = scheduledTime.split(":");
    const scheduledDate = new Date(
      now.getFullYear(),
      now.getMonth(),
      now.getDate(),
      hours,
      minutes,
      0
    );

    if (scheduledDate.getTime() < now.getTime()) {
      scheduledDate.setDate(scheduledDate.getDate() + 1);
    }

    const timeDiff = scheduledDate.getTime() - now.getTime();
    if (timeDiff < 0) {
      return "Time has passed";
    }

    const hoursLeft = Math.floor(timeDiff / (1000 * 60 * 60));
    const minutesLeft = Math.floor((timeDiff % (1000 * 60 * 60)) / (1000 * 60));
    return `${hoursLeft}h ${minutesLeft}m left`;
  };

  const handleTimeChange = (event) => {
    updateData("scheduledTime", event.target.value);
  };

  const handleActionChange = (event) => {
    setAction(event.target.value);
  };

  const handleSetSchedule = () => {
    if (!data.scheduledTime) {
      return;
    }
    const newMessage = {
      time: data.scheduledTime,
      timeLeft: calculateTimeLeft(data.scheduledTime),
      action: action,
    };

    const updatedMessages = [...scheduledMessages, newMessage];
    setScheduledMessages(updatedMessages);
    localStorage.setItem("scheduledMessages", JSON.stringify(updatedMessages));
    updateData("scheduledTime", "");

    const state = action === "Turn On" ? 1 : 0;
    const mqttData = JSON.stringify({
      time: data.scheduledTime,
      state: state,
      delete: false,
    });
    sendDataToFeed(mqttData, "schedule");
  };

  const removeMessage = (index) => {
    const messageToRemove = scheduledMessages[index];

    const updatedMessages = scheduledMessages.filter((_, i) => i !== index);
    setScheduledMessages(updatedMessages);
    localStorage.setItem("scheduledMessages", JSON.stringify(updatedMessages));

    const state = messageToRemove.action === "Turn On" ? 1 : 0;
    const mqttDeleteData = JSON.stringify({
      time: messageToRemove.time,
      state: state,
      delete: true,
    });
    sendDataToFeed(mqttDeleteData, "schedule");
  };

  return (
    <div className="scheduleContainer">
      <div className="inputContainer">
        <label className="scheduleLabel">
          Schedule Time:
          <input
            type="time"
            className="timeInput"
            value={data.scheduledTime || ""}
            onChange={handleTimeChange}
          />
        </label>
        <select
          className="actionSelect"
          onChange={handleActionChange}
          defaultValue="Turn On"
        >
          <option value="Turn On">Turn On</option>
          <option value="Turn Off">Turn Off</option>
        </select>
        <button className="setScheduleButton" onClick={handleSetSchedule}>
          Set Schedule
        </button>
      </div>
      <div className="messagesContainer">
        {scheduledMessages.map((message, index) => (
          <div key={index} className="message">
            <span className="messageContent">
              {message.time} - {message.action}, {message.timeLeft}
            </span>
            <Trash
              className="removeButton"
              onClick={() => removeMessage(index)}
            />
          </div>
        ))}
      </div>
    </div>
  );
}

export default Schedule;

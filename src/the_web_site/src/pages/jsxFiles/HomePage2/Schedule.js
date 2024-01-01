import { useState, useEffect } from "react";
import Clock from "react-live-clock";
import { useData } from "../../DataContext";

function Schedule() {
  const { data, updateData } = useData();
  const [timeLeft, setTimeLeft] = useState("");
  const [isScheduled, setIsScheduled] = useState(false);

  useEffect(() => {
    const storedTime = localStorage.getItem("scheduledTime");
    if (storedTime) {
      updateData("scheduledTime", storedTime);
      setIsScheduled(true);
    }
  }, []);

  useEffect(() => {
    let interval;
    if (isScheduled && data.scheduledTime) {
      interval = setInterval(() => {
        const remainingTime = calculateTimeLeft(data.scheduledTime);
        setTimeLeft(remainingTime);
      }, 1000);
    }

    return () => clearInterval(interval);
  }, [isScheduled, data.scheduledTime]);

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

    return `${hoursLeft} hours, ${minutesLeft} minutes`;
  };

  const handleTimeChange = (event) => {
    updateData("scheduledTime", event.target.value);
  };

  const handleSetSchedule = () => {
    setIsScheduled(true);
    localStorage.setItem("scheduledTime", data.scheduledTime);
    console.log(`Scheduled Time: ${data.scheduledTime}`);
  };

  return (
    <div>
      <Clock format={"hh:mm:ss A"} ticking={true} />
      <div>
        <label>
          Schedule Time:
          <input
            type="time"
            value={data.scheduledTime || ""}
            onChange={handleTimeChange}
          />
        </label>
        <button onClick={handleSetSchedule}>Set Schedule</button>
      </div>
      <div>Time Left: {timeLeft}</div>
    </div>
  );
}

export default Schedule;

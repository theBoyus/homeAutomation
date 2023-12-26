import HomePageFunctions from "./HomePageFunc";

const { ManualSwitch, Schedule, LightBased, SystemControl } = HomePageFunctions;

const OptionContent = ({
  selectedOption,
  startTime,
  endTime,
  onTimeChange,
  onEndTimeChange,
  onApplySettings,
  onResetTimers,
  onButtonClick,
}) => {
  switch (selectedOption) {
    case "Manual Switch":
      return <ManualSwitch onButtonClick={onButtonClick} />;
    case "Schedule":
      return (
        <Schedule
          startTime={startTime}
          endTime={endTime}
          onTimeChange={onTimeChange}
          onEndTimeChange={onEndTimeChange}
          onApplySettings={onApplySettings}
          onResetTimers={onResetTimers}
        />
      );
    case "Light-based":
      return <LightBased onButtonClick={onButtonClick} />;
    case "System control":
      return <SystemControl onButtonClick={onButtonClick} />;
    default:
      return null;
  }
};

export default OptionContent;

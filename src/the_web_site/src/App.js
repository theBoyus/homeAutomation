import "./App.css";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import HomePage from "./pages/jsxFiles/HomePage";
import Toolbar from "./pages/jsxFiles/Toolbar";
import Graphs from "./pages/jsxFiles/Graphs";
import About from "./pages/jsxFiles/About";
import AdafruitIO from "./MQTT/AdafruitIO";

function App() {
  return (
    <Router>
      <Toolbar />
      <div className="main-content">
        <Routes>
          <Route path="/" element={<HomePage />} />
          <Route path="/Graphs" element={<Graphs />} />
          <Route path="/About" element={<About />} />
          <Route path="/AdafruitIO" element={<AdafruitIO />} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;

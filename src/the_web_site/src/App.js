import React, { useState, useEffect } from 'react';
import { BrowserRouter as Router, Routes, Route, Navigate } from "react-router-dom";
import HomePage from "./pages/jsxFiles/HomePage";
import Toolbar from "./pages/jsxFiles/Toolbar";
import Graphs from "./pages/jsxFiles/Graphs";
import About from "./pages/jsxFiles/About";
import AdafruitIO from "./MQTT/AdafruitIO";
import SignInComponent from "./pages/jsxFiles/SignInComponent";
import { AuthProvider, useAuth } from './firebase/useAuth';
import "./App.css";
import { DataProvider } from './pages/DataContext';

function App() {
  return (
    <AuthProvider>
      <DataProvider>
        <Router>
          <AppRoutes />
        </Router>
      </DataProvider>
    </AuthProvider>
  );
}

export default App;

const AppRoutes = () => {
  const { currentUser } = useAuth();
  const [isLoading, setIsLoading] = useState(true);

  useEffect(() => {
    setIsLoading(currentUser === undefined);
  }, [currentUser]);

  if (isLoading) {
    return <div>Loading...</div>;
  }

    return (
    <>
      {currentUser && <Toolbar />}
      <div className="main-content">
        <Routes>
          {currentUser ? (
            <>
              <Route path="/" element={<HomePage />} />
              <Route path="/Graphs" element={<Graphs />} />
              <Route path="/About" element={<About />} />
              <Route path="/AdafruitIO" element={<AdafruitIO />} />
              <Route path="/SignIn" element={<SignInComponent />} />
            </>
          ) : (
            <>
              <Route path="/SignIn" element={<SignInComponent />} />
              <Route path="*" element={<Navigate replace to="/SignIn" />} />
            </>
          )}
        </Routes>
      </div>
    </>
  );
};
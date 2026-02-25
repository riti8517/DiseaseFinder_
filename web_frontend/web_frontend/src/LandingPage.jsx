import { useState, useEffect } from "react";
import docImage from "./assets/doc.png";
import "./App.css";

export default function LandingPage({ onSelect }) {
  const [darkMode, setDarkMode] = useState(() => localStorage.getItem("darkMode") === "true");

  useEffect(() => {
    document.body.classList.toggle("dark-mode", darkMode);
    localStorage.setItem("darkMode", darkMode);
  }, [darkMode]);

  return (
    <div className={`app-container landing-container ${darkMode ? "dark" : ""}`}>
      <div className="mh-top-bar" style={{ justifyContent: "flex-end" }}>
        <button
          className="dark-mode-toggle"
          onClick={() => setDarkMode(!darkMode)}
          title={darkMode ? "Switch to light mode" : "Switch to dark mode"}
        >
          {darkMode ? "☀️" : "🌙"}
        </button>
      </div>

      <header className="app-header landing-header">
        <img src={docImage} alt="Health Assistant" className="app-logo" />
        <h1 className="app-title">Health Assistant</h1>
        <p className="app-subtitle">Your personal guide to understanding your health</p>
      </header>

      <main className="landing-main">
        <p className="landing-question">How can we help you today?</p>

        <div className="landing-cards">
          {/* Physical Health */}
          <button className="landing-card physical-card" onClick={() => onSelect("physical")}>
            <div className="landing-card-icon">🩺</div>
            <div className="landing-card-content">
              <h2>Physical Health</h2>
              <p>Identify possible illnesses based on your symptoms using our AI-powered disease finder.</p>
              <span className="landing-card-cta">Find possible disease →</span>
            </div>
          </button>

          {/* Mental Health */}
          <button className="landing-card mental-card" onClick={() => onSelect("mental")}>
            <div className="landing-card-icon">🧠</div>
            <div className="landing-card-content">
              <h2>Mental Health</h2>
              <p>Get support, resources, and AI-guided advice for your mental wellbeing and emotional health.</p>
              <span className="landing-card-cta">Get support →</span>
            </div>
          </button>
        </div>

        <p className="landing-disclaimer">
          ⚠️ This tool is for informational purposes only and does not replace professional medical advice.
        </p>
      </main>

      <footer className="app-footer">
        <p>&copy; 2025 Health Assistant. All rights reserved.</p>
      </footer>
    </div>
  );
}

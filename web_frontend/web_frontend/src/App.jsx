import React, { useEffect, useRef, useState } from "react";
import "./App.css";
import Pill from "./components/Pill";
import Chatbot from "./Chatbot";
import docImage from "./assets/doc.png";

// Disease information database
const diseaseInfo = {
  "Common Cold": {
    severity: "Mild",
    description: "A viral infection of the upper respiratory tract affecting the nose and throat.",
    treatments: ["Rest", "Fluids", "Over-the-counter cold medications", "Throat lozenges"],
    duration: "7-10 days"
  },
  "Flu": {
    severity: "Moderate",
    description: "A contagious respiratory illness caused by influenza viruses.",
    treatments: ["Antiviral medications", "Rest", "Fluids", "Pain relievers"],
    duration: "1-2 weeks"
  },
  "Migraine": {
    severity: "Moderate",
    description: "A neurological condition causing intense, debilitating headaches.",
    treatments: ["Pain relievers", "Triptans", "Rest in dark room", "Preventive medications"],
    duration: "4-72 hours per episode"
  },
  "Diabetes": {
    severity: "Chronic",
    description: "A metabolic disease causing high blood sugar levels over a prolonged period.",
    treatments: ["Insulin therapy", "Oral medications", "Diet management", "Regular exercise"],
    duration: "Lifelong management"
  },
  "Hypertension": {
    severity: "Chronic",
    description: "A condition where blood pressure against artery walls is too high.",
    treatments: ["Blood pressure medications", "Low-sodium diet", "Exercise", "Stress management"],
    duration: "Lifelong management"
  }
};

const getDefaultDiseaseInfo = (diseaseName) => ({
  severity: "Consult Doctor",
  description: `${diseaseName} — Please consult a healthcare provider for detailed information about this condition.`,
  treatments: ["Consult a healthcare provider for proper treatment"],
  duration: "Varies"
});

// Quick-select common symptoms — names must exactly match the Java backend's CacheManager
const QUICK_SYMPTOMS = [
  { id: "q1",  symptom: "high fever" },
  { id: "q2",  symptom: "headache" },
  { id: "q3",  symptom: "cough" },
  { id: "q4",  symptom: "fatigue" },
  { id: "q5",  symptom: "nausea" },
  { id: "q6",  symptom: "vomiting" },
  { id: "q7",  symptom: "diarrhoea" },
  { id: "q8",  symptom: "throat irritation" },
  { id: "q9",  symptom: "runny nose" },
  { id: "q10", symptom: "muscle pain" },
  { id: "q11", symptom: "dizziness" },
  { id: "q12", symptom: "chest pain" },
];

// Emergency symptom combinations that warrant urgent care
const EMERGENCY_KEYWORDS = [
  "chest pain",
  "difficulty breathing",
  "shortness of breath",
  "sudden numbness",
  "severe headache",
  "loss of consciousness",
  "coughing blood",
  "high fever",
];

export default function App() {
  const [searchTerm, setSearchTerm] = useState("");
  const [suggestions, setSuggestions] = useState([]);
  const [selectedSymptoms, setSelectedSymptoms] = useState([]);
  const [selectedSymptomSet, setSelectedSymptomSet] = useState(new Set());
  const [activeSuggestion, setActiveSuggestion] = useState(0);
  const [predictedDisease, setPredictedDisease] = useState("");
  const [isLoading, setIsLoading] = useState(false);
  const [darkMode, setDarkMode] = useState(() => localStorage.getItem("darkMode") === "true");
  const [isEmergency, setIsEmergency] = useState(false);
  const [chatTrigger, setChatTrigger] = useState(null);

  const inputRef = useRef(null);

  // Apply dark mode to body
  useEffect(() => {
    document.body.classList.toggle("dark-mode", darkMode);
    localStorage.setItem("darkMode", darkMode);
  }, [darkMode]);

  // Detect emergency symptoms
  useEffect(() => {
    const names = selectedSymptoms.map((s) => s.symptom.toLowerCase());
    const found = names.some((n) => EMERGENCY_KEYWORDS.some((k) => n.includes(k)));
    setIsEmergency(found);
  }, [selectedSymptoms]);

  // Autocomplete fetch
  useEffect(() => {
    if (!searchTerm.trim()) { setSuggestions([]); return; }
    fetch("/symptoms")
      .then((res) => res.json())
      .then((data) => {
        const filtered = data
          .filter((s) => s.symptom.toLowerCase().includes(searchTerm.toLowerCase()))
          .map((s, i) => ({ ...s, id: `api-${i}-${s.symptom}` }));
        setActiveSuggestion(0);
        setSuggestions(filtered);
      })
      .catch(console.error);
  }, [searchTerm]);

  const handleSelectSymptom = (symptom) => {
    if (selectedSymptomSet.has(symptom.symptom)) return;
    setSelectedSymptoms((prev) => [...prev, symptom]);
    setSelectedSymptomSet((prev) => new Set([...prev, symptom.symptom]));
    setSearchTerm("");
    setSuggestions([]);
    inputRef.current?.focus();
  };

  const handleRemoveSymptom = (symptom) => {
    setSelectedSymptoms((prev) => prev.filter((s) => s.symptom !== symptom.symptom));
    setSelectedSymptomSet((prev) => {
      const copy = new Set(prev);
      copy.delete(symptom.symptom);
      return copy;
    });
  };

  const handleClearAll = () => {
    setSelectedSymptoms([]);
    setSelectedSymptomSet(new Set());
    setPredictedDisease("");
    setIsEmergency(false);
    inputRef.current?.focus();
  };

  const handleKeyDown = (e) => {
    if (e.key === "Backspace" && !e.target.value && selectedSymptoms.length) {
      handleRemoveSymptom(selectedSymptoms[selectedSymptoms.length - 1]);
    } else if (e.key === "ArrowDown" && suggestions.length) {
      e.preventDefault();
      setActiveSuggestion((i) => Math.min(i + 1, suggestions.length - 1));
    } else if (e.key === "ArrowUp" && suggestions.length) {
      e.preventDefault();
      setActiveSuggestion((i) => Math.max(i - 1, 0));
    } else if (e.key === "Enter" && suggestions.length) {
      e.preventDefault();
      handleSelectSymptom(suggestions[activeSuggestion]);
    }
  };

  const handleSearchDisease = () => {
    const symptomNames = selectedSymptoms.map((s) => s.symptom).join(",");
    const url = `/predictDisease?symptoms=${encodeURIComponent(symptomNames)}`;
    setIsLoading(true);
    setPredictedDisease("");
    fetch(url)
      .then((res) => res.json())
      .then((data) => { setPredictedDisease(data.data); setIsLoading(false); })
      .catch((err) => { console.error(err); setIsLoading(false); });
  };

  const handleDiscussWithAI = () => {
    const symptomList = selectedSymptoms.map((s) => s.symptom).join(", ");
    const message = `I was predicted to have "${predictedDisease}" based on these symptoms: ${symptomList}. Can you explain this condition, what causes it, and what I should do next?`;
    setChatTrigger(message);
  };

  const getDiseaseDetails = (disease) => diseaseInfo[disease] || getDefaultDiseaseInfo(disease);

  const getSeverityColor = (severity) => ({
    "Mild": "#48bb78",
    "Moderate": "#ed8936",
    "Chronic": "#e53e3e",
    "Consult Doctor": "#667eea"
  }[severity] || "#667eea");

  return (
    <>
      <div className={`app-container ${darkMode ? "dark" : ""}`}>
        <header className="app-header">
          <button
            className="dark-mode-toggle"
            onClick={() => setDarkMode(!darkMode)}
            title={darkMode ? "Switch to light mode" : "Switch to dark mode"}
          >
            {darkMode ? "☀️" : "🌙"}
          </button>
          <img src={docImage} alt="Disease Finder" className="app-logo" />
          <h1 className="app-title">Disease Finder</h1>
          <p className="app-subtitle">
            Enter your symptoms below and we'll help identify possible conditions
          </p>
        </header>

        {/* How it works */}
        <div className="how-it-works">
          <div className="step"><span className="step-num">1</span><span>Select your symptoms</span></div>
          <div className="step-arrow">→</div>
          <div className="step"><span className="step-num">2</span><span>Click predict</span></div>
          <div className="step-arrow">→</div>
          <div className="step"><span className="step-num">3</span><span>Get results & AI advice</span></div>
        </div>

        <main className="app-main">
          {/* Emergency Banner */}
          {isEmergency && (
            <div className="emergency-banner">
              <span className="emergency-icon">🚨</span>
              <div>
                <strong>Seek Emergency Care Immediately</strong>
                <p>One or more of your symptoms may require urgent medical attention. Please call emergency services or go to the nearest emergency room.</p>
              </div>
            </div>
          )}

          <div className="search-section">
            {/* Quick symptom chips */}
            <div className="quick-symptoms-section">
              <p className="quick-label">Common symptoms — click to add:</p>
              <div className="quick-chips">
                {QUICK_SYMPTOMS.map((s) => (
                  <button
                    key={s.id}
                    className={`quick-chip ${selectedSymptomSet.has(s.symptom) ? "selected" : ""}`}
                    onClick={() => handleSelectSymptom(s)}
                    disabled={selectedSymptomSet.has(s.symptom)}
                  >
                    {s.symptom}
                  </button>
                ))}
              </div>
            </div>

            <div className="search-box-wrapper">
              <div className="search-box-header">
                <span className="symptom-counter">
                  {selectedSymptoms.length > 0
                    ? `${selectedSymptoms.length} symptom${selectedSymptoms.length > 1 ? "s" : ""} selected`
                    : "No symptoms selected"}
                </span>
                {selectedSymptoms.length > 0 && (
                  <button className="clear-all-btn" onClick={handleClearAll}>
                    Clear all
                  </button>
                )}
              </div>

              <div className="search-box">
                <div className="pills-container">
                  {selectedSymptoms.map((s) => (
                    <Pill key={s.id} text={s.symptom} onClick={() => handleRemoveSymptom(s)} />
                  ))}
                </div>
                <input
                  ref={inputRef}
                  className="search-input"
                  value={searchTerm}
                  onChange={(e) => setSearchTerm(e.target.value)}
                  placeholder="Type a symptom (e.g. headache, fever)..."
                  onKeyDown={handleKeyDown}
                />
                {searchTerm && suggestions.length > 0 && (
                  <ul className="suggestions-list">
                    {suggestions.map((symptom, idx) =>
                      !selectedSymptomSet.has(symptom.symptom) ? (
                        <li
                          key={symptom.id}
                          className={idx === activeSuggestion ? "active" : ""}
                          onClick={() => handleSelectSymptom(symptom)}
                        >
                          {symptom.symptom}
                        </li>
                      ) : null
                    )}
                  </ul>
                )}
              </div>
            </div>

            <button
              className="predict-btn"
              onClick={handleSearchDisease}
              disabled={selectedSymptoms.length === 0 || isLoading}
            >
              {isLoading ? <span className="loading-spinner"></span> : "Find Possible Disease"}
            </button>

            {selectedSymptoms.length === 0 && (
              <p className="hint-text">Start typing or click a common symptom above</p>
            )}
          </div>

          {/* Result card */}
          {predictedDisease && (
            <div className="result-card">
              <div className="result-card-header">Prediction Result</div>
              <div className="result-card-body">
                <div className="disease-header">
                  <h3 className="disease-name">{predictedDisease}</h3>
                  <span
                    className="severity-badge"
                    style={{ backgroundColor: getSeverityColor(getDiseaseDetails(predictedDisease).severity) }}
                  >
                    {getDiseaseDetails(predictedDisease).severity}
                  </span>
                </div>

                <p className="disease-description">{getDiseaseDetails(predictedDisease).description}</p>

                <div className="disease-info-section">
                  <h4>Common Treatments</h4>
                  <ul className="treatment-list">
                    {getDiseaseDetails(predictedDisease).treatments.map((t, i) => (
                      <li key={i}>{t}</li>
                    ))}
                  </ul>
                </div>

                <div className="disease-info-section">
                  <h4>Typical Duration</h4>
                  <p>{getDiseaseDetails(predictedDisease).duration}</p>
                </div>

                {/* Action buttons */}
                <div className="result-actions">
                  <button className="action-btn ai-btn" onClick={handleDiscussWithAI}>
                    💬 Discuss with AI
                  </button>
                  <button className="action-btn reset-btn" onClick={handleClearAll}>
                    🔄 Start over
                  </button>
                </div>

                <p className="disease-disclaimer">
                  ⚠️ This is for informational purposes only. Please consult a healthcare provider for proper diagnosis and treatment.
                </p>
              </div>
            </div>
          )}
        </main>

        <footer className="app-footer">
          <p>&copy; 2025 Disease Finder. All rights reserved.</p>
        </footer>
      </div>

      <Chatbot triggerMessage={chatTrigger} onTriggerHandled={() => setChatTrigger(null)} />
    </>
  );
}

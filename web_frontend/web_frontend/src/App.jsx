import React, { useEffect, useRef, useState } from "react";
import "./App.css";
import Pill from "./components/Pill";
import Chatbot from "./Chatbot";          // ← NEW import
import docImage from "./assets/doc.png";

export default function App() {
  const [searchTerm, setSearchTerm] = useState("");
  const [suggestions, setSuggestions] = useState([]);
  const [selectedSymptoms, setSelectedSymptoms] = useState([]);
  const [selectedSymptomSet, setSelectedSymptomSet] = useState(new Set());
  const [activeSuggestion, setActiveSuggestion] = useState(0);
  const [predictedDisease, setPredictedDisease] = useState("");

  const inputRef = useRef(null);
  const currentUrl = new URL(window.location.href);

  /* ----------------- fetch suggestions ----------------- */
  useEffect(() => {
    if (!searchTerm.trim()) {
      setSuggestions([]);
      return;
    }

    const apiUrl = `http://${currentUrl.hostname}:8080/symptoms`;

    fetch(apiUrl)
      .then((res) => res.json())
      .then((data) => {
        const filtered = data.filter((s) =>
          s.symptom.toLowerCase().includes(searchTerm.toLowerCase())
        );
        setActiveSuggestion(0);
        setSuggestions(filtered);
      })
      .catch(console.error);
  }, [searchTerm]);

  /* ------------------- chip helpers -------------------- */
  const handleSelectSymptom = (symptom) => {
    setSelectedSymptoms((prev) => [...prev, symptom]);
    setSelectedSymptomSet((prev) => new Set([...prev, symptom.symptom]));
    setSearchTerm("");
    setSuggestions([]);
    inputRef.current.focus();
  };

  const handleRemoveSymptom = (symptom) => {
    setSelectedSymptoms((prev) =>
      prev.filter((s) => s.id !== symptom.id)
    );
    setSelectedSymptomSet((prev) => {
      const copy = new Set(prev);
      copy.delete(symptom.symptom);
      return copy;
    });
  };

  /* ------------------- keyboard UX --------------------- */
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

  /* ---------------- disease prediction ----------------- */
  const handleSearchDisease = () => {
    const symptomNames = selectedSymptoms.map((s) => s.symptom).join(",");
    const url = `http://${currentUrl.hostname}:8080/predictDisease?symptoms=${encodeURIComponent(
      symptomNames
    )}`;

    fetch(url)
      .then((res) => res.json())
      .then((data) => setPredictedDisease(data.data))
      .catch(console.error);
  };

  /* ---------------------- UI --------------------------- */
  return (
    <>
      {/* Disease‑Finder main card */}
      <div className="app-container">
        <header>
          <img src={docImage} alt="Disease Finder" className="app-image" />
          <h1>Disease Finder</h1>
        </header>

        <main>
          {/* symptom search */}
          <div className="symptom-search-container">
            <div className="symptom-search-input">
              {selectedSymptoms.map((s) => (
                <Pill
                  key={s.id}
                  text={s.symptom}
                  onClick={() => handleRemoveSymptom(s)}
                />
              ))}

              <input
                ref={inputRef}
                value={searchTerm}
                onChange={(e) => setSearchTerm(e.target.value)}
                placeholder="Search for symptoms…"
                onKeyDown={handleKeyDown}
              />

              <button type="button" onClick={handleSearchDisease}>
                Search Disease
              </button>

              {searchTerm && (
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

          {/* prediction card */}
          {predictedDisease && (
            <div className="predicted-disease-card">
              <h2>Prediction Result</h2>
              <div className="disease-details">
                <div>
                  <h3>{predictedDisease}</h3>
                  <p>
                    Based on your symptoms, this is the most likely disease.
                    Please consult a healthcare provider for confirmation.
                  </p>
                </div>
              </div>
            </div>
          )}
        </main>

        <footer>
          <p>&copy; 2025 Disease Finder. All rights reserved.</p>
        </footer>
      </div>

      {/* floating chatbot (outside main card) */}
      <Chatbot />
    </>
  );
}

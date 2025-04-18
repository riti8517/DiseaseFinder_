import React, { useEffect, useRef, useState } from "react";
import "./App.css";
import Pill from "./components/Pill";
import docImage from "./assets/doc.png";

function App() {
  const [searchTerm, setSearchTerm] = useState("");
  const [suggestions, setSuggestions] = useState([]);
  const [selectedSymptoms, setSelectedSymptoms] = useState([]);
  const [selectedSymptomSet, setSelectedSymptomSet] = useState(new Set());
  const [activeSuggestion, setActiveSuggestion] = useState(0);
  const [predictedDisease, setPredictedDisease] = useState("");

  const inputRef = useRef(null);
  const currentUrl = new URL(window.location.href);

  // Fetch symptoms based on search term
  useEffect(() => {
    const fetchSymptoms = () => {
      setActiveSuggestion(0);
      if (searchTerm.trim() === "") {
        setSuggestions([]);
        return;
      }
      const apiUrl = `http://${currentUrl.hostname}:8080/symptoms`;

      fetch(apiUrl)
        .then((res) => res.json())
        .then((data) => {
          const filteredSymptoms = data.filter((symptom) =>
            symptom.symptom.toLowerCase().includes(searchTerm.toLowerCase())
          );
          setSuggestions(filteredSymptoms);
        })
        .catch((err) => {
          console.error(err);
        });
    };

    fetchSymptoms();
  }, [searchTerm]);

  // Select and remove symptoms
  const handleSelectSymptom = (symptom) => {
    setSelectedSymptoms([...selectedSymptoms, symptom]);
    setSelectedSymptomSet(new Set([...selectedSymptomSet, symptom.symptom]));
    setSearchTerm("");
    setSuggestions([]);
    inputRef.current.focus();
  };

  const handleRemoveSymptom = (symptom) => {
    const updatedSymptoms = selectedSymptoms.filter(
      (selectedSymptom) => selectedSymptom.id !== symptom.id
    );
    setSelectedSymptoms(updatedSymptoms);
    setSelectedSymptomSet(new Set(updatedSymptoms.map((s) => s.symptom)));
  };

  const handleKeyDown = (e) => {
    if (e.key === "Backspace" && e.target.value === "" && selectedSymptoms.length > 0) {
      const lastSymptom = selectedSymptoms[selectedSymptoms.length - 1];
      handleRemoveSymptom(lastSymptom);
      setSuggestions([]);
    } else if (e.key === "ArrowDown" && suggestions.length > 0) {
      e.preventDefault();
      setActiveSuggestion((prevIndex) =>
        prevIndex < suggestions.length - 1 ? prevIndex + 1 : prevIndex
      );
    } else if (e.key === "ArrowUp" && suggestions.length > 0) {
      e.preventDefault();
      setActiveSuggestion((prevIndex) => (prevIndex > 0 ? prevIndex - 1 : 0));
    } else if (
      e.key === "Enter" &&
      activeSuggestion >= 0 &&
      activeSuggestion < suggestions.length
    ) {
      handleSelectSymptom(suggestions[activeSuggestion]);
    }
  };

  // Search for disease based on symptoms
  const handleSearchDisease = () => {
    const symptomNames = selectedSymptoms.map((symptom) => symptom.symptom).join(",");
    const predictUrl = `http://${currentUrl.hostname}:8080/predictDisease?symptoms=${encodeURIComponent(symptomNames)}`;
    
    fetch(predictUrl)
      .then((res) => res.json())
      .then((data) => {
        setPredictedDisease(data.data);
        
        document.getElementById("pd").innerHTML = "Predicted Disease: " +data.data;
        
      })
      .catch((err) => {
        console.error(err);
      });
  };


  return (
    <div className="app-container">
      <header>
        <img src={docImage} alt="Disease Finder" className="app-image" />
        <h1>Disease Finder</h1>
      </header>

      <main>
        {/* Symptom Search Section */}
        <div className="symptom-search-container">
          <div className="symptom-search-input">
            {selectedSymptoms.map((symptom) => (
              <Pill
                key={symptom.id}
                text={symptom.symptom}
                onClick={() => handleRemoveSymptom(symptom)}
              />
            ))}

            <input
              ref={inputRef}
              type="text"
              value={searchTerm}
              onChange={(e) => setSearchTerm(e.target.value)}
              placeholder="Search for symptoms..."
              onKeyDown={handleKeyDown}
            />
            <button type="button" onClick={handleSearchDisease}>
              Search Disease
            </button>

            {searchTerm && (
              <ul className="suggestions-list">
                {suggestions.map((symptom, index) => {
                  return !selectedSymptomSet.has(symptom.symptom) ? (
                    <li
                      className={index === activeSuggestion ? "active" : ""}
                      key={symptom.id}
                      onClick={() => handleSelectSymptom(symptom)}
                    >
                      {symptom.symptom}
                    </li>
                  ) : null;
                })}
              </ul>
            )}
          </div>
        </div>

        {/* Predicted Disease Section */}
        <div id="predicted-disease">
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
        </div>
      </main>

      <footer>
        <p>&copy; 2025 Disease Finder. All rights reserved.</p>
      </footer>
    </div>
  );
}

export default App;

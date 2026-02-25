import { useState, useEffect } from "react";
import Chatbot from "./Chatbot";
import "./App.css";

const MOODS = [
  { id: "great",   label: "Great",    emoji: "😊" },
  { id: "okay",    label: "Okay",     emoji: "😐" },
  { id: "anxious", label: "Anxious",  emoji: "😰" },
  { id: "sad",     label: "Sad",      emoji: "😢" },
  { id: "angry",   label: "Angry",    emoji: "😤" },
  { id: "tired",   label: "Exhausted","emoji": "😴" },
];

const TOPICS = [
  { id: "anxiety",    label: "Anxiety",          icon: "💭", description: "Worry, panic attacks, nervousness" },
  { id: "depression", label: "Depression",        icon: "🌧️", description: "Low mood, loss of interest, hopelessness" },
  { id: "stress",     label: "Stress",            icon: "🔥", description: "Overwhelmed, burnout, tension" },
  { id: "sleep",      label: "Sleep Issues",      icon: "🌙", description: "Insomnia, oversleeping, poor sleep" },
  { id: "grief",      label: "Grief & Loss",      icon: "💔", description: "Bereavement, loss, sadness" },
  { id: "self",       label: "Self-Esteem",       icon: "🪞", description: "Confidence, self-worth, body image" },
];

const RESOURCES = [
  { name: "Crisis Text Line",       detail: "Text HOME to 741741",           icon: "💬" },
  { name: "National Suicide Prevention Lifeline", detail: "Call 988",        icon: "📞" },
  { name: "SAMHSA Helpline",        detail: "1-800-662-4357 (free, 24/7)",   icon: "🏥" },
  { name: "Crisis Chat",            detail: "crisischat.org",                icon: "🌐" },
];

export default function MentalHealth({ onBack }) {
  const [darkMode, setDarkMode] = useState(() => localStorage.getItem("darkMode") === "true");
  const [selectedMood, setSelectedMood] = useState(null);
  const [selectedTopic, setSelectedTopic] = useState(null);
  const [chatTrigger, setChatTrigger] = useState(null);

  useEffect(() => {
    document.body.classList.toggle("dark-mode", darkMode);
    localStorage.setItem("darkMode", darkMode);
  }, [darkMode]);

  const handleTalkAboutTopic = (topic) => {
    setSelectedTopic(topic);
    setChatTrigger(
      `I'm struggling with ${topic.label.toLowerCase()}. ${topic.description}. Can you provide some support, coping strategies, and advice to help me manage this?`
    );
  };

  const handleMoodChat = (mood) => {
    setSelectedMood(mood);
    setChatTrigger(
      `I'm feeling ${mood.label.toLowerCase()} ${mood.emoji} today. Can you help me understand why I might feel this way and what I can do to improve my mental wellbeing?`
    );
  };

  return (
    <>
      <div className={`app-container mental-container ${darkMode ? "dark" : ""}`}>
        {/* Top controls */}
        <div className="mh-top-bar">
          <button className="back-btn" onClick={onBack}>← Back</button>
          <button
            className="dark-mode-toggle"
            onClick={() => setDarkMode(!darkMode)}
            title={darkMode ? "Switch to light mode" : "Switch to dark mode"}
          >
            {darkMode ? "☀️" : "🌙"}
          </button>
        </div>

        <header className="app-header">
          <div className="mh-header-icon">🧠</div>
          <h1 className="app-title">Mental Health Support</h1>
          <p className="app-subtitle">You're not alone. Let's talk about how you're feeling.</p>
        </header>

        <main className="app-main">
          {/* Mood check-in */}
          <section className="mh-section">
            <h2 className="mh-section-title">How are you feeling today?</h2>
            <div className="mood-grid">
              {MOODS.map((mood) => (
                <button
                  key={mood.id}
                  className={`mood-btn ${selectedMood?.id === mood.id ? "selected" : ""}`}
                  onClick={() => handleMoodChat(mood)}
                >
                  <span className="mood-emoji">{mood.emoji}</span>
                  <span className="mood-label">{mood.label}</span>
                </button>
              ))}
            </div>
          </section>

          {/* Topic selection */}
          <section className="mh-section">
            <h2 className="mh-section-title">What would you like to talk about?</h2>
            <div className="topics-grid">
              {TOPICS.map((topic) => (
                <button
                  key={topic.id}
                  className={`topic-card ${selectedTopic?.id === topic.id ? "selected" : ""}`}
                  onClick={() => handleTalkAboutTopic(topic)}
                >
                  <span className="topic-icon">{topic.icon}</span>
                  <div className="topic-text">
                    <strong>{topic.label}</strong>
                    <small>{topic.description}</small>
                  </div>
                </button>
              ))}
            </div>
          </section>

          {/* Crisis resources */}
          <section className="mh-section mh-resources">
            <h2 className="mh-section-title emergency-title">🚨 Need immediate help?</h2>
            <div className="resources-grid">
              {RESOURCES.map((r, i) => (
                <div key={i} className="resource-card">
                  <span className="resource-icon">{r.icon}</span>
                  <div>
                    <strong>{r.name}</strong>
                    <p>{r.detail}</p>
                  </div>
                </div>
              ))}
            </div>
          </section>
        </main>

        <footer className="app-footer">
          <p>&copy; 2025 Health Assistant. All rights reserved.</p>
        </footer>
      </div>

      <Chatbot triggerMessage={chatTrigger} onTriggerHandled={() => setChatTrigger(null)} />
    </>
  );
}

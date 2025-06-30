import React, { useState, useRef, useEffect } from "react";
import "./Chatbot.css";

export default function Chatbot() {
  const [open, setOpen] = useState(false);
  const [messages, setMessages] = useState([
    { from: "bot", text: "Hi! How can I help?" },
  ]);
  const [text, setText] = useState("");
  const endRef = useRef(null);

  useEffect(() => {
    endRef.current?.scrollIntoView({ behavior: "smooth" });
  }, [messages]);

  const send = async () => {
    if (!text.trim()) return;

    const userMsg = { from: "user", text };
    setMessages((m) => [...m, userMsg]);
    setText("");

    try {
      const res = await fetch(
        `http://${window.location.hostname}:11434/api/chat`,
        {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({
            model: "llama3",
            messages: [
              { role: "system", content: "You are a helpful medical AI assistant." },
              ...messages.map((m) => ({
                role: m.from === "user" ? "user" : "assistant",
                content: m.text,
              })),
              { role: "user", content: userMsg.text },
            ],
            stream: false,
          }),
        }
      );

      const data = await res.json();
      setMessages((m) => [...m, { from: "bot", text: data.message.content }]);
    } catch (err) {
      console.error(err);
   
    }
  };

  const handleKey = (e) => {
    if (e.key === "Enter") {
      e.preventDefault();
      send();
    }
  };

  return (
    <>
      {}
      {!open && (
        <button className="chat-toggle" onClick={() => setOpen(true)}>
          💬
        </button>
      )}

      {}
      {open && (
        <div className="chat-box">
          <div className="chat-header">
            Chat
            <button className="close-btn" onClick={() => setOpen(false)}>
              ✕
            </button>
          </div>

          <div className="chat-body">
            {messages.map((m, i) => (
              <div key={i} className={`msg ${m.from}`}>
                {m.text}
              </div>
            ))}
            <div ref={endRef} />
          </div>

          <div className="chat-input-area">
            <input
              value={text}
              placeholder="Type and hit Enter…"
              onChange={(e) => setText(e.target.value)}
              onKeyDown={handleKey}
            />
            <button onClick={send}>Send</button>
          </div>
        </div>
      )}
    </>
  );
}

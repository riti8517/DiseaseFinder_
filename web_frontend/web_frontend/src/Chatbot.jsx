import { useState, useRef, useEffect } from "react";
import "./Chatbot.css";

const BACKEND_URL = "";

export default function Chatbot({ triggerMessage, onTriggerHandled }) {
  const [open, setOpen] = useState(false);
  const [messages, setMessages] = useState([
    { from: "bot", text: "Hi! I'm your AI medical assistant. How can I help you today?" },
  ]);
  const [text, setText] = useState("");
  const [isLoading, setIsLoading] = useState(false);
  const endRef = useRef(null);
  const messagesRef = useRef(messages);

  useEffect(() => { messagesRef.current = messages; }, [messages]);

  useEffect(() => {
    endRef.current?.scrollIntoView({ behavior: "smooth" });
  }, [messages]);

  const sendMessage = async (msgText) => {
    if (!msgText.trim() || isLoading) return;

    const userMsg = { from: "user", text: msgText };
    setMessages((m) => [...m, userMsg]);
    setIsLoading(true);

    try {
      const res = await fetch(`${BACKEND_URL}/chat`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          history: messagesRef.current.map((m) => ({
            role: m.from === "user" ? "user" : "assistant",
            content: m.text,
          })),
          question: msgText,
        }),
      });
      const data = await res.json();
      setMessages((m) => [...m, { from: "bot", text: data.answer }]);
    } catch (err) {
      console.error(err);
      setMessages((m) => [...m, { from: "bot", text: "Sorry, something went wrong." }]);
    } finally {
      setIsLoading(false);
    }
  };

  // Handle external trigger (e.g. "Discuss with AI" button)
  useEffect(() => {
    if (!triggerMessage) return;
    setOpen(true);
    sendMessage(triggerMessage);
    onTriggerHandled?.();
  }, [triggerMessage]);

  const send = () => {
    if (!text.trim() || isLoading) return;
    sendMessage(text);
    setText("");
  };

  const handleKey = (e) => {
    if (e.key === "Enter") { e.preventDefault(); send(); }
  };

  return (
    <>
      {!open && (
        <button className="chat-toggle" onClick={() => setOpen(true)}>
          💬
        </button>
      )}

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
            {isLoading && (
              <div className="msg bot typing">
                <span className="typing-dot"></span>
                <span className="typing-dot"></span>
                <span className="typing-dot"></span>
              </div>
            )}
            <div ref={endRef} />
          </div>

          <div className="chat-input-area">
            <input
              value={text}
              placeholder="Type and hit Enter…"
              onChange={(e) => setText(e.target.value)}
              onKeyDown={handleKey}
              disabled={isLoading}
            />
            <button onClick={send} disabled={isLoading}>
              {isLoading ? "..." : "Send"}
            </button>
          </div>
        </div>
      )}
    </>
  );
}

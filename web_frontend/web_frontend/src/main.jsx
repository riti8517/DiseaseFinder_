import React, { useState } from "react";
import ReactDOM from "react-dom/client";
import LandingPage from "./LandingPage.jsx";
import App from "./App.jsx";
import MentalHealth from "./MentalHealth.jsx";

function Root() {
  const [page, setPage] = useState("landing");

  if (page === "physical") return <App onBack={() => setPage("landing")} />;
  if (page === "mental")   return <MentalHealth onBack={() => setPage("landing")} />;
  return <LandingPage onSelect={setPage} />;
}

ReactDOM.createRoot(document.getElementById("root")).render(
  <React.StrictMode>
    <Root />
  </React.StrictMode>
);

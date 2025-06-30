
export default function Pill({ text, onClick }) {
  return (
    <span className="symptom-pill" onClick={onClick}>
      {text} &times;
    </span>
  );
}

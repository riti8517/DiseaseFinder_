const Pill = ({ text, onClick }) => {
    return (
      <span className="symptom-pill" onClick={onClick}>
        <span>{text} ×</span>
      </span>
    );
  };
  
  export default Pill;
  
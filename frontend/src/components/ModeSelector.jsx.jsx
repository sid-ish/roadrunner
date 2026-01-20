export default function ModeSelector({ mode, setMode }) {
  return (
    <div style={{ display: "flex", gap: 8 }}>
      {["video", "live", "photo"].map(m => (
        <button
          key={m}
          className={mode === m ? "btn" : "btn btn-outline"}
          onClick={() => setMode(m)}
        >
          {m.toUpperCase()}
        </button>
      ))}
    </div>
  );
}

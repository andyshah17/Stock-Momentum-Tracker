import React, { useState } from "react";
<div className="app-container">
   {/* your UI */}
</div>

function App() {
  const [ticker, setTicker] = useState("");
  const [data, setData] = useState(null);
  const [error, setError] = useState("");

  const fetchStockData = async () => {
    setError("");
    setData(null);

    try {
      const response = await fetch(`http://127.0.0.1:5000/momentum/${ticker}`);
      const json = await response.json();

      if (!response.ok) {
        setError(json.error || "Something went wrong.");
        return;
      }

      setData(json);
    } catch (e) {
      setError("Cannot connect to backend.");
    }
  };

  return (
    <div className="app-container">
      <h1>📈 Stock Momentum Tracker</h1>

      <input
        type="text"
        placeholder="Enter ticker symbol (AAPL)"
        value={ticker}
        onChange={(e) => setTicker(e.target.value.toUpperCase())}
        style={{
          padding: "10px",
          fontSize: "16px",
          borderRadius: "5px",
          marginRight: "10px",
        }}
      />

      <button
        onClick={fetchStockData}
        style={{
          padding: "10px 20px",
          backgroundColor: "#61dafb",
          border: "none",
          borderRadius: "5px",
          cursor: "pointer",
        }}
      >
        Search
      </button>

      {error && <p style={{ marginTop: "20px", color: "red" }}>{error}</p>}

      {data && (
        <div
          style={{
            marginTop: "30px",
            padding: "20px",
            border: "1px solid #444",
            display: "inline-block",
            textAlign: "left",
            borderRadius: "10px",
            backgroundColor: "#222",
          }}
        >
          <h2>{data.ticker}</h2>
          <p>Latest Price: ${data.latest_price}</p>
          <p>7-Day Momentum: {data.momentum_7d}</p>
          <p>30-Day Momentum: {data.momentum_30d}</p>
        </div>
      )}
    </div>
  );
}

export default App;

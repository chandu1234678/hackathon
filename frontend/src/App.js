import './App.css';
import { useState } from 'react';

const API_BASE_URL = process.env.REACT_APP_API_BASE_URL || 'http://localhost:8000';

function App() {
  const [text, setText] = useState('');
  const [prediction, setPrediction] = useState(null);
  const [confidence, setConfidence] = useState(null);
  const [error, setError] = useState('');
  const [loading, setLoading] = useState(false);

  const handlePredict = async () => {
    if (!text.trim()) {
      setError('Please enter clinical notes or patient text.');
      return;
    }

    setLoading(true);
    setError('');

    try {
      const response = await fetch(`${API_BASE_URL}/api/predict`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ text }),
      });

      if (!response.ok) {
        throw new Error(`Request failed with status ${response.status}`);
      }

      const data = await response.json();
      setPrediction(data.prediction);
      setConfidence(data.confidence);
    } catch (requestError) {
      setError(requestError.message || 'Unable to fetch prediction');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="app-shell">
      <div className="card">
        <h1>Diabetic Ulcer AI Dashboard</h1>
        <p className="subtitle">Enter clinical text to run model inference.</p>

        <textarea
          value={text}
          onChange={(event) => setText(event.target.value)}
          rows={6}
          placeholder="Example: Patient has non-healing ulcer with mild infection signs..."
        />

        <button onClick={handlePredict} disabled={loading}>
          {loading ? 'Predicting...' : 'Predict'}
        </button>

        {error && <p className="error">{error}</p>}

        {prediction !== null && confidence !== null && (
          <div className="result">
            <p><strong>Prediction:</strong> {prediction}</p>
            <p><strong>Confidence:</strong> {confidence}</p>
          </div>
        )}
      </div>
    </div>
  );
}

export default App;

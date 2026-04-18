import React, { useState } from 'react';

export default function App() {
  const [file, setFile] = useState(null);
  const [loading, setLoading] = useState(false);
  const [data, setData] = useState(null);

  const handleUpload = async () => {
    if (!file) return;
    setLoading(true);
    
    const formData = new FormData();
    formData.append('file', file);

    const response = await fetch('http://localhost:8000/analyze', {
      method: 'POST',
      body: formData,
    });
    
    const result = await response.json();
    setData(result);
    setLoading(false);
  };

  return (
    <div className="min-h-screen bg-gray-900 text-white p-10 font-sans">
      <header className="mb-10">
        <h1 className="text-4xl font-black text-blue-500">AttentionX AI</h1>
        <p className="text-gray-400">Multimodal Creator Intelligence</p>
      </header>

      <div className="bg-gray-800 p-8 rounded-xl border border-gray-700">
        <input type="file" onChange={(e) => setFile(e.target.files[0])} className="mb-4" />
        <button 
          onClick={handleUpload}
          className="bg-blue-600 px-6 py-2 rounded-lg font-bold hover:bg-blue-700 transition"
          disabled={loading}
        >
          {loading ? "Analyzing..." : "Process Video"}
        </button>
      </div>

      {data && (
        <div className="mt-10 grid grid-cols-2 gap-10">
          <div className="bg-gray-800 p-5 rounded-lg">
            <h2 className="text-xl font-bold mb-4">Transcript</h2>
            {data.transcript.map((t, i) => <p key={i} className="text-sm mb-2 text-gray-300">{t.text}</p>)}
          </div>
          <div className="bg-gray-800 p-5 rounded-lg">
            <h2 className="text-xl font-bold mb-4">Face Tracking Data</h2>
            <p className="text-green-400">Active frames analyzed: {data.visuals.length}</p>
          </div>
        </div>
      )}
    </div>
  );
}
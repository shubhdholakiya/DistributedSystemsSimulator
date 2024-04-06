import React, { useState, useEffect } from 'react';
import './App.css';

function App() {
  const [nodes, setNodes] = useState([]);

  useEffect(() => {
    // Fetch nodes from the backend on component mount
    fetch('/nodes')
      .then(response => response.json())
      .then(data => setNodes(data));
  }, []);

  const simulateCommunication = () => {
    // Trigger communication simulation
    fetch('/simulate/communication', { method: 'POST' })
      .then(response => response.json())
      .then(data => alert(JSON.stringify(data)));
  };

  return (
    <div className="App">
      <header className="App-header">
        <p>Distributed Systems Simulator</p>
        {nodes.map(node => (
          <div key={node.id}>Node {node.id}: {node.status}</div>
        ))}
        <button onClick={simulateCommunication}>Simulate Communication</button>
      </header>
    </div>
  );
}

export default App;

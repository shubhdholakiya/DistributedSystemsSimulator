import React, { useState, useEffect } from 'react';
import './App.css';
import BarChart from './BarChart';

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
    fetch(`${process.env.REACT_APP_API_URL}/simulate/communication`, {
      method: 'POST',
    })
    .then(response => response.json())
    .then(data => console.log(data))
    .catch(error => console.error('Error:', error));
  };

  return (
    <div className="App">
      <header className="App-header">
        <p>Distributed Systems Simulator</p>

        {nodes.map(node => (
          <div key={node.id}>
            Node {node.id}: {node.status}
          </div>
        ))}

        {nodes.length > 0 && (
          <BarChart 
            labels={nodes.map(node => `Node ${node.id}`)} 
            dataPoints={nodes.map(node => node.status)} 
          />
        )}

        <button onClick={simulateCommunication}>Simulate Communication</button>
      </header>
    </div>
  );
}

export default App;

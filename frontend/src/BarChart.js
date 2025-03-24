import React from 'react';
import { Bar } from 'react-chartjs-2';
import 'chart.js/auto';

const BarChart = ({ labels, dataPoints }) => {
  const data = {
    labels: labels,
    datasets: [{
      label: 'Nodes Status',
      data: dataPoints,
      backgroundColor: ['rgba(255, 99, 132, 0.2)', 'rgba(54, 162, 235, 0.2)'],
      borderColor: ['rgba(255,99,132,1)', 'rgba(54, 162, 235, 1)'],
      borderWidth: 1
    }]
  };

  return <Bar data={data} />;
};

export default BarChart;

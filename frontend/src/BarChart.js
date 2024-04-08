import React from 'react';
import { Bar } from 'react-chartjs-2';
import 'chart.js/auto';

const BarChart = () => {
  const data = {
    labels: ['Label 1', 'Label 2'],
  datasets: [{
    label: 'Dataset 1',
    data: [value1, value2],
    backgroundColor: ['rgba(255, 99, 132, 0.2)', 'rgba(54, 162, 235, 0.2)'],
    borderColor: ['rgba(255,99,132,1)', 'rgba(54, 162, 235, 1)'],
    borderWidth: 1
    }]
  };

  return <Bar data={data} key={Date.now()} />;
};

export default BarChart;

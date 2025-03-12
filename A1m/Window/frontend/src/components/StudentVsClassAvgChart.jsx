import React from 'react';
import Chart from 'react-apexcharts';

const StudentVsClassAvgChart = ({ studentData, classData }) => {
  // Extract dates and averages
  const dates = studentData.map(test => Object.keys(test)[0]);
  const studentAvg = studentData.map(test => test[Object.keys(test)[0]].Avg_of_test);
  const classAvg = classData.map(test => test[Object.keys(test)[0]].Avg_of_class);

  const options = {
    chart: {
      type: 'line',
      height: 350,
      toolbar: { show: false },
      animations: {
        enabled: true,
        easing: 'easeout',
        speed: 800,
      },
    },
    stroke: {
      curve: 'smooth',
      width: 3,
    },
    xaxis: {
      categories: dates,
      labels: {
        style: {
          colors: '#6B7280',
          fontSize: '12px',
          fontWeight: 500,
        },
      },
      tickAmount: Math.min(10, dates.length),
    },
    yaxis: {
      min: 0,
      max: 100,
      labels: {
        style: {
          colors: '#6B7280',
          fontSize: '12px',
          fontWeight: 500,
        },
      },
    },
    colors: ['#1E90FF', '#FF5733'],
    fill: {
      type: 'gradient',
      gradient: {
        shade: 'light',
        type: 'vertical',
        shadeIntensity: 0.4,
        gradientToColors: ['#00BFFF', '#FF8C00'],
        stops: [0, 100],
      },
    },
    markers: {
      size: 5,
      colors: ['#1E90FF', '#FF5733'],
      strokeWidth: 2,
      strokeColors: ['#ffffff'],
      hover: { size: 7 },
    },
    legend: {
      position: 'top',
      fontSize: '14px',
      fontWeight: 'bold',
      labels: { colors: '#374151' },
    },
    tooltip: {
      theme: 'dark',
      x: { format: 'dd MMM yyyy' },
    },
    grid: {
      borderColor: '#E5E7EB',
      strokeDashArray: 5,
    },
  };

  const series = [
    {
      name: 'Student Average',
      data: studentAvg,
    },
    {
      name: 'Class Average',
      data: classAvg,
    },
  ];

  return (
    <div className="bg-white p-6 rounded-lg shadow-xl border border-gray-200">
      <h2 className="text-xl font-semibold text-gray-700 mb-4">
        📊 Student vs Class Performance
      </h2>
      <Chart options={options} series={series} type="line" height={350} />
    </div>
  );
};

export default StudentVsClassAvgChart;

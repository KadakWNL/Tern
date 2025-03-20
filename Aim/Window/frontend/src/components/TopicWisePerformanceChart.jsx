import React from 'react';
import Chart from 'react-apexcharts';

const TopicWisePerformanceChart = ({ studentData, classData, isStatic = false, bw = false }) => {
  if (!studentData || !classData) {
    return <div className="text-center text-gray-500">Loading topic data...</div>;
  }

  const topics = Object.keys(studentData);
  const studentScores = topics.map(topic => {
    const latestTest = Object.keys(studentData[topic]).pop(); // Get the latest test key
    return studentData[topic][latestTest]; // Get the latest test score
  });
  const classScores = topics.map(topic => {
    const latestTest = Object.keys(classData[topic]).pop(); // Get the latest class score
    return classData[topic][latestTest];
  });

  // Conditional color modes
  const colors = bw 
  ? ['#6B7280', '#9CA3AF']  // Grayscale Mode (Dark Gray & Medium Gray)
  : ['#050535', '#64748B']; // Deep Navy & Slate Gray

const fillColors = bw 
  ? ['#F3F4F6', '#E5E7EB']  // Very light grays for a clean look
  : ['#DDE1F2', '#EEF1F7']; // Soft blue-gray fills for subtle contrast

const strokeColor = bw ? '#8B8B8B' : '#64748B'; // Keep stroke clean and visible
const opacity = bw ? 0.7 : 0.3; // Lower opacity for a softer fill effect
  const options = {
    chart: {
      type: 'radar',
      animations: { enabled: !isStatic },
      toolbar: { show: false },
      fontFamily: 'inherit',
    },
    title: {
      text: 'Topic-wise Performance',
      align: 'center',
      style: {
        fontSize: '16px',
        fontWeight: 'bold',
        color: bw ? '#4B5563' : '#000', // Text color based on mode
      },
    },
    xaxis: {
      categories: topics,
      labels: {
        style: {
          fontSize: '12px',
          fontWeight: 'bold',
          color: bw ? '#4B5563' : '#000',
        },
      },
    },
    yaxis: {
      min: 0,
      max: 100,
      labels: {
        show: true,
        style: {
          fontSize: '10px',
          color: bw ? '#4B5563' : '#000',
        },
      },
    },
    colors: colors,
    legend: {
      position: 'top',
      fontSize: '12px',
      fontWeight: 'bold',
      offsetY: 0,
      labels: {
        colors: bw ? '#4B5563' : '#000',
      },
    },
    markers: {
      size: 4,
    },
    stroke: {
      width: 2,
    },
    fill: {
      opacity: opacity,
    },
    dataLabels: {
      enabled: false,
    },
    tooltip: {
      enabled: true,
    },
    plotOptions: {
      radar: {
        size: 120,
        polygons: {
          strokeColors: strokeColor,
          fill: {
            colors: fillColors,
          },
        },
      },
    },
    responsive: [
      {
        breakpoint: 480,
        options: {
          plotOptions: {
            radar: {
              size: 100,
            },
          },
        },
      },
    ],
  };

  const series = [
    {
      name: 'Student',
      data: studentScores,
    },
    {
      name: 'Class',
      data: classScores,
    },
  ];

  return (
    <div>
      <Chart options={options} series={series} type="radar" height="100%" width="80%" />
    </div>
  );
};

export default TopicWisePerformanceChart;

import React from 'react';
import Chart from 'react-apexcharts';

const TopicWisePerformanceChart = ({ studentData, classData }) => {
    console.log(studentData)
    console.log(classData)
    const topics = Object.keys(studentData);
    const studentScores = topics.map(topic => {
      const latestTest = Object.keys(studentData[topic]).pop(); // Get the latest test key
      return studentData[topic][latestTest]; // Get the latest test score
    });
    const classScores = topics.map(topic => {
      const latestTest = Object.keys(classData[topic]).pop(); // Get the latest test key
      return classData[topic][latestTest]; // Get the latest class score
    });
    
  const options = {
    chart: {
      type: 'radar',
      height: 400, // SUPER BIG now
      width: '50%', // Uses full width
      toolbar: {
        show: false,
      },
    },
    title: {
      text: '📊 Topic-wise Performance',
      align: 'center',
      style: {
        fontSize: '22px',
        fontWeight: 'bold',
      },
    },
    xaxis: {
      categories: topics,
      labels: {
        style: {
          fontSize: '16px', // Bigger text
          fontWeight: 'bold',
        },
      },
    },
    yaxis: {
      min: 0,
      max: 100,
      labels: {
        style: {
          fontSize: '7px',
        },
      },
    },
    colors: ['#007AFF', '#FF5733'],
    legend: {
      position: 'top',
      fontSize: '16px',
      fontWeight: 'bold',
    },
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
    <div className="bg-white p-8 rounded-lg shadow-lg w-full">
      <Chart options={options} series={series} type="radar" height={700} />
    </div>
  );
};

export default TopicWisePerformanceChart;

import React from 'react';
import Chart from 'react-apexcharts';

const TopicWisePerformanceChart = ({ studentData, classData, isStatic=false }) => {
    if (!studentData || !classData) {
        return <div className="text-center text-gray-500">Loading topic data...</div>;
    }

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
      animations:{enabled:!isStatic},
      toolbar: {
        show: false,
      },
      fontFamily: 'inherit',
    },
    title: {
      text: 'Topic-wise Performance',
      align: 'center',
      style: {
        fontSize: '16px',
        fontWeight: 'bold',
      },
    },
    xaxis: {
      categories: topics,
      labels: {
        style: {
          fontSize: '12px',
          fontWeight: 'bold',
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
        },
      },
    },
    colors: ['#007AFF', '#FF5733'],
    legend: {
      position: 'top',
      fontSize: '12px',
      fontWeight: 'bold',
      offsetY: 0,
    },
    markers: {
      size: 4,
    },
    stroke: {
      width: 2,
    },
    fill: {
      opacity: 0.4,
    },
    dataLabels: {
      enabled: false,
    },
    tooltip: {
      enabled: true,
    },
    plotOptions: {
      radar: {
        size: 120, // This controls the size of the radar chart
        polygons: {
          strokeColors: '#e9e9e9',
          fill: {
            colors: ['#f8f8f8', '#fff']
          }
        }
      }
    },
    responsive: [
      {
        breakpoint: 480,
        options: {
          plotOptions: {
            radar: {
              size: 100
            }
          }
        }
      }
    ]
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
        <Chart 
          options={options} 
          series={series} 
          type="radar" 
          height="100%" 
          width="80%" 
        />
    </div>
  );
};

export default TopicWisePerformanceChart;
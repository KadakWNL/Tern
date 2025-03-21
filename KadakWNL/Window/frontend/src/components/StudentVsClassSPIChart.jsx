import React from 'react';
import Chart from 'react-apexcharts';

const StudentVsClassSPIChart = ({ studentSPI, classSPI, isStatic = false, bw = false }) => {
  let colors;
  if (!bw) {
    colors = ['#050535']; // Deep Navy
  } else {
    colors = ['#6B7280']; // Dark Gray for Grayscale Mode
  }

  const options = {
    chart: {
      type: 'bar',
      height: 170,
      animations: { enabled: !isStatic },
      toolbar: { show: false },
    },
    plotOptions: {
      bar: {
        horizontal: true,
        barHeight: '30%',
        borderRadius: 4, // Slight rounded bars for a smooth look
      },
    },
    xaxis: {
      categories: ['Class SPI', 'Student SPI'],
      max: 100,
      labels: {
        style: {
          fontSize: '12px',
          fontWeight: 500,
          color: bw ? '#4B5563' : '#000', // Dark gray text for labels
        },
      },
    },
    colors: colors,
    fill: {
      type: 'solid',
    },
    dataLabels: {
      enabled: true,
      style: {
        fontSize: '14px',
        fontWeight: 'bold',
      },
      formatter: (val) => val.toFixed(2),
    },
    tooltip: {
      theme: 'light',
    },
    grid: {
      borderColor: '#E5E7EB', // Light gray grid lines
    },
  };

  const series = [{ name: 'SPI', data: [classSPI, studentSPI] }];

  return (
    <div className="bg-white p-4s">
      <h3 className="text-lg font-semibold text-gray-700 mb-2">Student vs Class SPI</h3>
      <Chart options={options} series={series} type="bar" height={170} />
    </div>
  );
};

export default StudentVsClassSPIChart;

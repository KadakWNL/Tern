import React from 'react';
import Chart from 'react-apexcharts';

const StudentVsClassSPIChart = ({ studentSPI, classSPI,isStatic=false }) => {
  const options = {
    chart: {
      type: 'bar',
      height: 200,
      animations:{enabled:!isStatic},
      toolbar: { show: false },
    },
    plotOptions: {
      bar: {
        horizontal: true,
        barHeight: '30%',
      },
    },
    xaxis: {
      categories: ['Class SPI', 'Student SPI'],
      max: 100,
    },
    colors: ['#4F46E5', '#10B981'], // Blue & Green
    dataLabels: {
      enabled: true,
      style: {
        fontSize: '14px',
        fontWeight: 'bold',
      },
      formatter: (val) => val.toFixed(2),
    },
    tooltip: {
      theme: 'dark',
    },
    grid: {
      borderColor: '#e5e7eb',
    },
  };

  const series = [{ name: 'SPI', data: [classSPI, studentSPI] }];

  return (
    <div className="bg-white p-4 rounded-lg">
      <h3 className="text-lg font-semibold text-gray-700 mb-2">Student vs Class SPI</h3>
      <Chart options={options} series={series} type="bar" height={200} />
    </div>
  );
};

export default StudentVsClassSPIChart;

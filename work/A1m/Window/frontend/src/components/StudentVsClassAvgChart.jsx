import React from "react";
import Chart from "react-apexcharts";

const StudentVsClassAvgChart = ({ studentData, classData }) => {
  // Extract dates and averages
  const dates = studentData.map((test) => Object.keys(test)[0]);
  const studentAvg = studentData.map((test) => test[Object.keys(test)[0]].Avg_of_test);
  const classAvg = classData.map((test) => test[Object.keys(test)[0]].Avg_of_class);

  const options = {
    chart: {
      type: "line",
      height: 350,
      toolbar: { show: false },
      animations: {
        enabled: true,
        easing: "easeout",
        speed: 800,
      },
      background: "#ffffff", // White background
    },
    stroke: {
      curve: "smooth",
      width: 3,
    },
    xaxis: {
      categories: dates,
      labels: {
        style: {
          colors: "#6B7280", // Gray text
          fontSize: "12px",
          fontWeight: 500,
        },
      },
      tickAmount: Math.min(10, dates.length), // Limit the number of ticks
    },
    yaxis: {
      min: 0,
      max: 100,
      labels: {
        style: {
          colors: "#6B7280", // Gray text
          fontSize: "12px",
          fontWeight: 500,
        },
      },
    },
    colors: ["#3B82F6", "#EF4444"], // Blue and Red
    fill: {
      type: "gradient",
      gradient: {
        shade: "light",
        type: "vertical",
        shadeIntensity: 0.3,
        gradientToColors: ["#93C5FD", "#FCA5A5"], // Light blue and light red
        stops: [0, 100],
      },
    },
    markers: {
      size: 5,
      colors: ["#3B82F6", "#EF4444"], // Blue and Red
      strokeWidth: 2,
      strokeColors: ["#ffffff"], // White stroke
      hover: { size: 7 },
    },
    legend: {
      position: "top",
      fontSize: "14px",
      fontWeight: "bold",
      labels: { colors: "#374151" }, // Dark gray text
    },
    tooltip: {
      theme: "light", // Light theme for tooltip
      x: { format: "dd MMM yyyy" }, // Format date in tooltip
    },
    grid: {
      borderColor: "#E5E7EB", // Light gray grid lines
      strokeDashArray: 5, // Dashed grid lines
    },
  };

  const series = [
    {
      name: "Student Average",
      data: studentAvg,
    },
    {
      name: "Class Average",
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
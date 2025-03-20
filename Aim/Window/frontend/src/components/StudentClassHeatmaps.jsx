import React from "react";
import Chart from "react-apexcharts";

const StudentClassHeatmaps = ({ studentData, classData, bw = null, isStatic = false }) => {
  if (!studentData || !classData) {
    return <div className="text-center text-gray-500">Loading heatmap data... ⏳</div>;
  }

  // Extract unique test names from student data
  const testNames = [
    ...new Set(
      Object.values(studentData)
        .flatMap((topicData) => Object.keys(topicData))
    ),
  ];

  if (testNames.length === 0) {
    return <div className="text-center text-red-500">No test data available 😢</div>;
  }

  // Function to format data for ApexCharts
  const formatDataForHeatmap = (data) => {
    return Object.keys(data).map((topic) => ({
      name: topic,
      data: testNames.map((test) => ({
        x: test,
        y: Math.round(data[topic]?.[test] ?? null),
      })),
    }));
  };

  const studentSeries = formatDataForHeatmap(studentData);
  const classSeries = formatDataForHeatmap(classData);

  // Updated color scale
  const colorScale = {
    ranges: !bw
      ? [
        { from: 0, to: 31, color: "#888888", name: "Low" }, // Mid Gray
        { from: 31, to: 70, color: "#3A5BA4", name: "Medium" }, // Professional Royal Blue
        { from: 71, to: 100, color: "#050535", name: "High" }, // Deep Navy
        ]
      : [
          { from: 0, to: 30, color: "#E5E7EB", name: "Low" }, // Light Gray
          { from: 31, to: 70, color: "#888888", name: "Medium" }, // Mid Gray
          { from: 71, to: 100, color: "#222222", name: "High" }, // Dark Gray
        ],
  };

  const options = {
    chart: {
      type: "heatmap",
      height: 250,
      animations: { enabled: !isStatic },
      toolbar: { show: true },
    },
    plotOptions: {
      heatmap: {
        colorScale, // Using the dynamically assigned colorScale here
      },
    },
    dataLabels: {
      enabled: true,
      style: { colors: ["#ffffff"] }, // White text for better contrast
    },
    xaxis: {
      categories: testNames,
      labels: {
        rotate: -45,
        style: { fontSize: "10px", color: bw ? "#4B5563" : "#000000" },
      },
    },
    yaxis: {
      labels: { style: { fontSize: "12px", color: bw ? "#4B5563" : "#000000" } },
    },
  };

  return (
    <div>
      <h2 className="text-lg font-semibold mb-2 text-center">Topic Block Performance Comparison</h2>
      <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
        <div>
          <h3 className="text-md font-semibold mb-1">Student Performance</h3>
          <Chart options={options} series={studentSeries} type="heatmap" height={250} />
        </div>

        <div>
          <h3 className="text-md font-semibold mb-1">Class Average Performance</h3>
          <Chart options={options} series={classSeries} type="heatmap" height={250} />
        </div>
      </div>
    </div>
  );
};

export default StudentClassHeatmaps;

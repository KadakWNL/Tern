import React from "react";
import Chart from "react-apexcharts";

const StudentClassHeatmaps = ({ studentData, classData }) => {
  if (!studentData || !classData) {
    return <div className="text-center text-gray-500">Loading heatmap data... ⏳</div>;
  }

  // 🔥 Extract available test keys dynamically
  const testEntries = Object.entries(studentData);
  if (testEntries.length === 0) {
    return <div className="text-center text-red-500">No test data available 😢</div>;
  }

  const testNames = Object.keys(testEntries[testEntries.length - 1][1]); // Get test names from last test object
  if (testNames.length === 0) {
    return <div className="text-center text-red-500">No test data found 😭</div>;
  }

  // 🔥 Function to format data for ApexCharts
  const formatDataForHeatmap = (data) => {
    return Object.keys(data).map((topic) => ({
      name: topic, // Example: "Mechanics", "Optics", etc.
      data: testNames.map((test) => ({
        x: test,
        y: data[topic]?.[test] ?? null, // Ensure safe access to test scores
      })),
    }));
  };

  const studentSeries = formatDataForHeatmap(studentData);
  const classSeries = formatDataForHeatmap(classData);

  // 🔥 Check if data is actually being populated
  console.log("📊 Student Heatmap Data:", studentSeries);
  console.log("📊 Class Heatmap Data:", classSeries);

  // If no valid data, show a message instead of a broken chart
  if (studentSeries.length === 0 || classSeries.length === 0) {
    return <div className="text-center text-red-500">No heatmap data available 😭</div>;
  }

  // ApexCharts config
  const options = {
    chart: {
      type: "heatmap",
      height: 400,
    },
    plotOptions: {
      heatmap: {
        colorScale: {
          ranges: [
            { from: 0, to: 30, color: "#ff4d4d", name: "Low" },
            { from: 31, to: 70, color: "#fdd835", name: "Medium" },
            { from: 71, to: 100, color: "#00e676", name: "High" },
          ],
        },
      },
    },
    dataLabels: {
      enabled: true,
      style: { colors: ["#000"] },
    },
    xaxis: {
      categories: testNames,
      labels: { style: { fontSize: "14px" } },
    },
    yaxis: {
      labels: { style: { fontSize: "12px" } },
    },
    tooltip: {
      enabled: true,
    },
    title: {
      text: "📊 Topic Block Performance Heatmap",
      align: "center",
      style: { fontSize: "18px", fontWeight: "bold" },
    },
  };

  return (
    <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
      <div className="bg-white p-4 rounded-lg shadow-md">
        <h2 className="text-lg font-semibold mb-2">Student Performance</h2>
        <Chart options={options} series={studentSeries} type="heatmap" height={400} />
      </div>
      <div className="bg-white p-4 rounded-lg shadow-md">
        <h2 className="text-lg font-semibold mb-2">Class Average Performance</h2>
        <Chart options={options} series={classSeries} type="heatmap" height={400} />
      </div>
    </div>
  );
};

export default StudentClassHeatmaps;

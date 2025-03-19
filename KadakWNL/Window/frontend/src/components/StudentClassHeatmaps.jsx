import React from "react";
import Chart from "react-apexcharts";

const StudentClassHeatmaps = ({ studentData, classData }) => {
  if (!studentData || !classData) {
    return <div className="text-center text-gray-500">Loading heatmap data... ⏳</div>;
  }

  // 🔥 Extract unique test names from student data
  const testNames = [
    ...new Set(
      Object.values(studentData)
        .flatMap((topicData) => Object.keys(topicData))
    ),
  ];

  if (testNames.length === 0) {
    return <div className="text-center text-red-500">No test data available 😢</div>;
  }

  // 🔥 Function to format data for ApexCharts
  const formatDataForHeatmap = (data) => {
    return Object.keys(data).map((topic) => ({
      name: topic, // Example: "Mechanics", "Optics", etc.
      data: testNames.map((test) => ({
        x: test,
        y: Math.round(data[topic]?.[test] ?? null), // Round values & ensure safe access
      })),
    }));
  };

  const studentSeries = formatDataForHeatmap(studentData);
  const classSeries = formatDataForHeatmap(classData);



  // ApexCharts config
  const options = {
    chart: {
      type: "heatmap",
      height: 200,
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
      align: "left",
      style: { fontSize: "14px", fontWeight: "bold" },
    },
  };

  return (
    <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
      {/* Student Performance Heatmap */}
      <div className="bg-white p-4 rounded-lg shadow-md">
        <h2 className="text-lg font-semibold mb-2">Student Performance</h2>
        <Chart options={options} series={studentSeries} type="heatmap" height={400} />
      </div>

      {/* Class Performance Heatmap */}
      <div className="bg-white p-4 rounded-lg shadow-md">
        <h2 className="text-lg font-semibold mb-2">Class Average Performance</h2>
        <Chart options={options} series={classSeries} type="heatmap" height={400} />
      </div>
    </div>
  );
};

export default StudentClassHeatmaps;
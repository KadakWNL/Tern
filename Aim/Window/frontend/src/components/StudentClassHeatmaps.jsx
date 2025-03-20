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
  let allTestNames;
  // Function to format data for ApexCharts
  const formatDataForHeatmap = (data) => {
    // Get all test names
    allTestNames=[];
    allTestNames = testNames.slice();
    
    // Get the last two tests (assuming testNames is sorted chronologically)
    const lastTwoTests = allTestNames.slice(-2);
    
    // All other tests for calculating the average
    const remainingTests = allTestNames.slice(0, -2);
    
    return Object.keys(data).map((topic) => {
      // Calculate average for remaining tests
      let sum = 0;
      let count = 0;
      
      remainingTests.forEach((test) => {
        const value = data[topic]?.[test];
        if (value !== undefined && value !== null) {
          sum += value;
          count++;
        }
      });
      
      // Average of remaining tests (ensuring it's not null)
      const average = count > 0 ? Math.round(sum / count) : 0;
      
      // Ensure each value is valid to prevent blank columns
      const secondLatestValue = data[topic]?.[lastTwoTests[0]];
      const latestValue = data[topic]?.[lastTwoTests[1]];
      allTestNames=[lastTwoTests[1],lastTwoTests[0],"Average"];
      return {
        name: topic,
        data: [
          // First column: most recent test
          {
            x: lastTwoTests[1],
            y: Math.round(latestValue ?? 0)
          },
          // Second column: second most recent test
          {
            x: lastTwoTests[0],
            y: Math.round(secondLatestValue ?? 0)
          },
          // Third column: average of remaining tests
          {
            x: "Average",
            y: average
          }
        ]
      };
    });
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
        distributed: true, // Helps in evenly spacing the cells
        useFillColorAsStroke: false, // Optional: makes smaller cells more visible
        columnWidth: "60%", // Reduce this to make cells smaller horizontally
        rowHeight: "80%", // Reduce this to make cells smaller vertically
      },
    },
    dataLabels: {
      enabled: true,
      style: { colors: ["#ffffff"] }, // White text for better contrast
    },
    xaxis: {
      categories: allTestNames,
      labels: {
        rotate: -45,
        style: { fontSize: "10px", color: bw ? "#4B5563" : "#000000" },
      },
    },
    yaxis: {
      labels: { style: { fontSize: "12px", color: bw ? "#4B5563" : "#000000" } },
    },
    grid: {
      padding: { top: 5, right: 8, bottom: 5, left: 5 }, // Reduces gaps around the heatmap
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

import React from "react";
import Chart from "react-apexcharts";

const StudentVsClassAvgChart = ({ studentData, classData, isStatic = false, bw = false }) => {
  // Extract dates and averages
// Function to process student and class data safely
// This function safely processes student and class data for line graphs
const processDataForLineGraph = (studentData, classData) => {
  // Extract dates from student data
  const classDates = classData.map(item => Object.keys(item)[0]);
  const filteredDates=[];
  const studentDataMap = {};
  studentData.forEach(item => {
    const key = Object.keys(item)[0];
    // Use includes() method to check if the value exists in the array
    if(classDates.includes(key)){
      studentDataMap[key] = item[key]["Avg_of_test"];
      filteredDates.push(key);
    }
  });
  
  const classDataMap = {};
  classData.forEach(item => {
    const key = Object.keys(item)[0];
    if(filteredDates.includes(key)){
    classDataMap[key] = item[key]["Avg_of_class"];
    }
  });
  console.log(classDataMap)
  
  const studentPlots = [];
  Object.entries(studentDataMap).forEach(([date, score]) => {
    studentPlots.push({
      x: date.split('-')[0],
      y: score
    });
  });
  const classPlots=[];
  Object.entries(classDataMap).forEach(([date, score]) => {
    classPlots.push({
      x: date.split('-')[0],
      y: score
    });
  });
  console.log(studentPlots)
  console.log(classPlots)
  return {
    dates: filteredDates,
    studentAvg: studentPlots,
    classAvg: classPlots
  };
};


// Usage:
const { dates, studentAvg, classAvg } = processDataForLineGraph(studentData, classData);

  // Color Scheme
  let colors, fill;
  if (!bw) {
    colors = ["#050535", "#64748B"]; // Deep Navy & Slate Gray
    fill = {
      type: "gradient",
      gradient: {
        shade: "light",
        type: "vertical",
        shadeIntensity: 0.3,
        gradientToColors: ["#1E3A8A", "#94A3B8"], // Lighter navy & blue-gray
        stops: [0, 100],
      },
    };
  } else {
    colors = ["#6B7280", "#D1D5DB"]; // Grayscale Mode
    fill = {
      type: "solid",
      colors: colors,
    };
  }

  const options = {
    chart: {
      type: "line",
      height: 350,
      toolbar: { show: false },
      animations: {
        enabled: !isStatic,
        easing: "easeout",
        speed: 800,
      },
      background: "#ffffff",
    },
    title: {
      text: "Overtime Performance",
      align: "center",
      style: {
        fontSize: "16px",
        fontWeight: "bold",
        color: bw ? "#4B5563" : "#000",
      },
    },
    stroke: {
      curve: "smooth",
      width: 4,
    },
    xaxis: {
      categories: dates,
      labels: {
        style: {
          colors: "#6B7280",
          fontSize: "12px",
          fontWeight: 500,
        },
      },
      tickAmount: Math.min(10, dates.length),
    },
    yaxis: {
      min: 0,
      max: 100,
      labels: {
        style: {
          colors: "#6B7280",
          fontSize: "12px",
          fontWeight: 500,
        },
      },
    },
    colors: colors,
    fill: fill,
    markers: {
      size: 5,
      colors: colors,
      strokeWidth: 3,
      strokeColors: ["#ffffff"],
      hover: { size: 7 },
    },
    legend: {
      position: "top",
      fontSize: "14px",
      fontWeight: "bold",
      labels: { colors: "#374151" },
    },
    tooltip: {
      theme: "light",
      x: { format: "dd MMM yyyy" },
    },
    grid: {
      borderColor: "#E5E7EB",
      strokeDashArray: 5,
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
    <div>
      <Chart options={options} series={series} type="line" height={350} />
    </div>
  );
};

export default StudentVsClassAvgChart;

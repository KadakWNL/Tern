import React from "react";
import StudentClassHeatmaps from "./components/StudentClassHeatmaps";
import StudentVsClassAvgChart from "./components/StudentVsClassAvgChart";
import StudentVsClassSPIChart from "./components/StudentVsClassSPIChart";
import TopicWisePerformanceChart from "./components/TopicWisePerformanceChart";
import studentData from "./Data/242021.json";
import classData from "./Data/common_data.json";

export default function GraphReportApp() {
  if (!studentData || !classData) {
    return <div className="text-center text-gray-500">Loading data...</div>;
  }

  const studentSPI = studentData[studentData.length - 1][Object.keys(studentData[studentData.length - 1])[0]].Avg_SPI_till_date;
  const classSPI = classData[classData.length - 1][Object.keys(classData[classData.length - 1])[0]].Avg_SPI_of_class_till_date;

  return (
    <div className="p-6 bg-gray-100 min-h-screen">
      <h1 className="text-2xl font-bold mb-4">Graph Report Dashboard</h1>
      <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
        <StudentVsClassAvgChart studentData={studentData} classData={classData} />
        <TopicWisePerformanceChart studentData={studentData} classData={classData} />
      </div>
      <div className="grid grid-cols-1 md:grid-cols-2 gap-4 mt-6">
        <StudentClassHeatmaps studentData={studentData} classData={classData} />
      </div>
      <div className="bg-white p-4 rounded-lg shadow-md mt-6">
        <StudentVsClassSPIChart studentSPI={studentSPI} classSPI={classSPI} />
      </div>
    </div>
  );
}

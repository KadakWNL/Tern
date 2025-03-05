import { useEffect, useState } from "react";
import axios from "axios";
import React from "react";
const DataDisplay = () => {
  const [data, setData] = useState(null);

  useEffect(() => {
    axios.get("http://127.0.0.1:8000/api/data")
      .then(response => setData(response.data))
      .catch(error => console.error("Error fetching data:", error));
  }, []);

  if (!data) return <p>Loading...</p>;

  return (
    <div className="p-6 bg-white rounded-lg shadow-md">
      <h2 className="text-xl font-bold text-gray-800">Student Info</h2>
      <p className="text-gray-600">Name: {data.student_name}</p>
      <p className="text-gray-600">Roll No: {data.roll_no}</p>
      <h3 className="text-lg font-semibold mt-4">Scores</h3>
      <p>SPI: {data.metrics.SPI}</p>
    </div>
  );
};

export default DataDisplay;

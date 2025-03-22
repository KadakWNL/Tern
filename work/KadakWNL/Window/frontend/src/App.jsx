import { Routes, Route, Link } from "react-router-dom";
import React, { useState, useEffect } from "react";
import HomePage from "./components/HomePage";
import ReplicaHomePage from "./components/ReplicaHomePage";
import BWReplicaHomePage from "./components/BWReplicaHomePage";

const App = () => {
  const [studentData, setStudentData] = useState(null);
  const [classData, setClassData] = useState(null);
  const [studentInfo, setStudentInfo] = useState(null);
  const [isLoading, setIsLoading] = useState(true);

  // Fetch all data
  useEffect(() => {
    const fetchAllData = async () => {
      setIsLoading(true);
      try {
        // Fetch files data
        const filesResponse = await fetch("http://localhost:8000/api/files");
        const filesData = await filesResponse.json();
        setStudentData(filesData.file1 || []);
        setClassData(filesData.file2 || []);
        
        // Fetch student info
        const infoResponse = await fetch("http://localhost:8000/api/data");
        const infoData = await infoResponse.json();
        setStudentInfo(infoData);
        
        // All data fetched successfully
        setIsLoading(false);
      } catch (error) {
        console.error("Error fetching data:", error);
        setIsLoading(false); // Still set loading to false so UI isn't stuck
      }
    };
    
    fetchAllData();
  }, []);
  
  // This useEffect will run whenever studentData changes
  useEffect(() => {
    console.log("Updated studentData:", studentData);
  }, [studentData]);

  if (isLoading) {
    return <div>Loading data, please wait...</div>;
  }

  return (
    <div>
      {/* Define Routes */}
      <Routes>
        <Route path="/" element={<HomePage 
        studentData={studentData} 
        classData={classData} 
        studentInfo={studentInfo}
        />} />
        <Route 
          path="/report" 
          element={
            <ReplicaHomePage 
              studentData={studentData} 
              classData={classData} 
              studentInfo={studentInfo}
            />
          } 
        />
        <Route 
          path="/bwreport" 
          element={
            <BWReplicaHomePage 
            studentData={studentData} 
            classData={classData} 
            studentInfo={studentInfo}
            />
          }
        />
      </Routes>
    </div>
  );
};

export default App;
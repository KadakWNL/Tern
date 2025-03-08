import DataDisplay from "./components/DataDisplay";
import React from "react";
import ReportCard from "./ReportCard";
import Chart from "../src/components/Chart"
function App() {
  return (
    <div className="min-h-screen bg-gray-100 flex items-center justify-center">
            {/* <ReportCard /> */}
            <Chart/>
      {/* <DataDisplay /> */}

    </div>
  )
}

export default App;

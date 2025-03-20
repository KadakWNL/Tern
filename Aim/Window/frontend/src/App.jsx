import { Routes, Route, Link } from "react-router-dom";
import React from "react";
import HomePage from "./components/HomePage";
import ReplicaHomePage from "./components/ReplicaHomePage";
import BWReplicaHomePage from "./components/BWReplicaHomePage"
const App = () => {
  return (
    <div>
    <div>
      {/* Define Routes */}
      <Routes>
        <Route path="/" element={<HomePage />} />
        <Route path="/report" element={<ReplicaHomePage />} />
        <Route path="/bwreport" element={<BWReplicaHomePage/>}/>
      </Routes>
    </div>

    </div>
  );
};


export default App;

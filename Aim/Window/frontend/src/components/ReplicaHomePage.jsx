
import { Link } from "react-router-dom";
import React, { useRef } from 'react';
import StudentVsClassAvgChart from './StudentVsClassAvgChart';
import StudentVsClassSPIChart from './StudentVsClassSPIChart';
import TopicWisePerformanceChart from './TopicWisePerformanceChart';
import StudentClassHeatmaps from './StudentClassHeatmaps';
import studentData from '../Data/242021.json';
import classData from '../Data/common_data.json';
const current_subject = "PHYSICS";

const studentInfo = {
  name: "Shreyas",
  studentNo: "69",
  yearLevel: "1",
  course: "How to get bitches",
  major: "wiffing",
  term: "2 years"
};

const subjects = {
  "PHYSICS": {
      "Mechanics": [
          "Units and Measurements (PUC-I)",
          "Motion in a Straight Line (PUC-I)",
          "Motion in a Plane (PUC-I)",
          "Laws of Motion (PUC-I)",
          "Work, Energy and Power (PUC-I)",
          "System of Particles and Rotational Motion (PUC-I)",
          "Gravitation (PUC-I)",
          "Mechanical Properties of Solids (PUC-I)",
          "Mechanical Properties of Fluids (PUC-I)"
      ],
      "Thermodynamics and Kinetic Theory": [
          "Thermal Properties of Matter (PUC-I)",
          "Thermodynamics (PUC-I)",
          "Kinetic Theory (PUC-I)"
      ],
      "Waves and Oscillations": [
          "Oscillations (PUC-I)",
          "Waves (PUC-I)"
      ],
      "Electricity and Magnetism": [
          "Electric Charges and Fields (PUC-II)",
          "Electrostatic Potential and Capacitance (PUC-II)",
          "Current Electricity (PUC-II)",
          "Moving Charges and Magnetism (PUC-II)",
          "Magnetism and Matter (PUC-II)",
          "Electromagnetic Induction (PUC-II)",
          "Alternating Current (PUC-II)"
      ],
      "Optics": [
          "Electromagnetic Waves (PUC-II)",
          "Ray Optics and Optical Instruments (PUC-II)",
          "Wave Optics (PUC-II)"
      ],
      "Modern Physics": [
          "Dual Nature of Radiation and Matter (PUC-II)",
          "Atoms (PUC-II)",
          "Nuclei (PUC-II)",
          "Semiconductor Electronics Materials, Devices and Simple Circuits (PUC-II)"
      ]
  },
  "CHEMISTRY": {
      "Physical Chemistry": [
          "Some Basic Concepts of Chemistry (PUC-I)",
          "Structure of Atom (PUC-I)",
          "Classification of Elements and Periodicity in Properties (PUC-I)",
          "Chemical Bonding and Molecular Structure (PUC-I)",
          "Thermodynamics (PUC-I)",
          "Equilibrium (PUC-I)",
          "Redox Reactions (PUC-I)",
          "Solutions (PUC-II)",
          "Electrochemistry (PUC-II)",
          "Chemical Kinetics (PUC-II)"
      ],
      "Inorganic Chemistry": [
          "The d and f Block Elements (PUC-II)",
          "Coordination Compounds (PUC-II)"
      ],
      "Organic Chemistry": [
          "Organic Chemistry: Some Basic Principles and Techniques (PUC-I)",
          "Hydrocarbons (PUC-I)",
          "Haloalkanes and Haloarenes (PUC-II)",
          "Alcohols, Phenols and Ethers (PUC-II)",
          "Aldehydes, Ketones and Carboxylic Acids (PUC-II)",
          "Amines (PUC-II)",
          "Biomolecules (PUC-II)"
      ]
  },
  "MATHEMATICS": {
      "Algebra": [
          "Sets (PUC-I)",
          "Relations and Functions (PUC-I)",
          "Complex Numbers and Quadratic Equations (PUC-I)",
          "Linear Inequalities (PUC-I)",
          "Permutations and Combinations (PUC-I)",
          "Binomial Theorem (PUC-I)",
          "Sequences and Series (PUC-I)",
          "Matrices (PUC-II)",
          "Determinants (PUC-II)"
      ],
      "Trigonometry": [
          "Trigonometric Functions (PUC-I)",
          "Inverse Trigonometric Functions (PUC-II)"
      ],
      "Coordinate Geometry": [
          "Straight Lines (PUC-I)",
          "Conic Sections (PUC-I)",
          "Introduction to Three Dimensional Geometry (PUC-I)",
          "Three Dimensional Geometry (PUC-II)"
      ],
      "Calculus": [
          "Limits and Derivatives (PUC-I)",
          "Continuity and Differentiability (PUC-II)",
          "Application of Derivatives (PUC-II)",
          "Integrals (PUC-II)",
          "Application of Integrals (PUC-II)",
          "Differential Equations (PUC-II)"
      ],
      "Statistics and Probability": [
          "Statistics (PUC-I)",
          "Probability (PUC-I)",
          "Probability (PUC-II)"
      ],
      "Linear Programming": [
          "Linear Programming (PUC-II)"
      ],
      "Vector Algebra": [
          "Vector Algebra (PUC-II)"
      ]
  }
};



const groupByBlocks = (data, type) => {
  const groupedScores = {};

  data.forEach((test) => {
    const testKey = Object.keys(test)[0];
    const testData = test[testKey][`Avg_of_${type}_chapter_wise`];

    for (const subject in subjects) {
      for (const block in subjects[subject]) {
        if (subject == current_subject) {
          const chapters = subjects[subject][block];

          if (!groupedScores[block]) {
            groupedScores[block] = {};
          }

          let totalScore = 0, count = 0;

          chapters.forEach((chapter) => {
            if (testData[chapter] !== undefined) {
              totalScore += testData[chapter];
              count++;
            }
          });

          groupedScores[block][testKey] = count > 0 ? Math.round(totalScore / count) : null;
        }
      }
    }
  });

  return groupedScores;
};


const ReplicaHomePage = () => {
  if (!studentData || !classData) {
    return <div className="text-center text-gray-500">Loading data...</div>;
  }

  const studentSPI = studentData[studentData.length - 1][Object.keys(studentData[studentData.length - 1])[0]].Avg_SPI_till_date;
  const classSPI = classData[classData.length - 1][Object.keys(classData[classData.length - 1])[0]].Avg_SPI_of_class_till_date;

  const studentTopicData = groupByBlocks(studentData, 'student');
  const classTopicData = groupByBlocks(classData, 'class');


  return (
    <div className="w-full text-sm border-black border-2">
      <div className="bg-white overflow-hidden">
        {/* Header */}
        <div className="bg-blue-800 text-white py-8 flex items-center justify-center">
          <div className="flex items-center">
            <div className="mr-4">
              <div className="w-12 h-12 relative">
                <div className="absolute inset-0 border-2 border-white rounded-full flex items-center justify-center">
                  <span className="text-xl font-bold">M</span>
                </div>
                <div className="absolute inset-0 border-2 border-white rounded-full rotate-45 border-l-transparent border-b-transparent"></div>
              </div>
            </div>
            <h1 className="text-xl font-bold">Manyu Classes</h1>
          </div>
        </div>
  
        {/* Report Title */}
        <div className="bg-cream-50 py-2 text-center">
          <h1 className="text-lg font-bold text-blue-800">REPORT CARD</h1>
          <div className="border-t border-blue-800 mx-16 mt-2"></div>
        </div>
  
        {/* Student Info */}
        <div className="bg-cream-50 px-32 grid grid-cols-2 gap-12 justify-center text-lg">
          <div>
            <div><b>Student Name:</b> {studentInfo.name}</div>
            <div><b>Student No.:</b> {studentInfo.studentNo}</div>
            <div><b>Year Level:</b> {studentInfo.yearLevel}</div>
          </div>
          <div>
            <div><b>Course:</b> {studentInfo.course}</div>
            <div><b>Major:</b> {studentInfo.major}</div>
            <div><b>Term:</b> {studentInfo.term}</div>
          </div>
        </div>
  
        {/* Charts */}
        
  {/* First Row: Two charts side by side */}

                <div className="grid grid-cols-2 lg:grid-cols-2 gap-4 justify-center shadow-md rounded-lg p-4">
                    <StudentVsClassAvgChart studentData={studentData} classData={classData} />
                    <TopicWisePerformanceChart studentData={studentTopicData} classData={classTopicData}/>
                </div>
            


            {/* Second Row: Full-width Heatmap */}
            <div className="bg-white p-2 rounded shadow w-full">
                <StudentClassHeatmaps studentData={studentTopicData} classData={classTopicData} isStatic={true} />
            </div>

            {/* Third Row: Full-width SPI Chart */}
            <div className="bg-white p-2 rounded shadow w-full">
                <StudentVsClassSPIChart studentSPI={studentSPI} classSPI={classSPI} isStatic={true} />
            </div>
            <div className="grid place-items-center text-lg p-5">
                <div>Some important Information</div>
            </div>

        {/* Footer */}
        <div className="bg-cream-50 p-2 flex justify-between items-center">
          <img src="/api/placeholder/80/40" alt="Institute Logo" className="h-10" />
          <img src="/api/placeholder/80/40" alt="Tern Logo" className="h-10" />
        </div>
        <div className="h-8 bg-blue-800 flex items-center justify-center text-white text-xs">
          made with ❤️ by Tern
        </div>
      </div>
    </div>
  );
};

export default ReplicaHomePage;
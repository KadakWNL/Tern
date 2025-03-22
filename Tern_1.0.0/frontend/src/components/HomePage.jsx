import React, { useRef } from 'react';
import StudentVsClassAvgChart from './StudentVsClassAvgChart';
import StudentVsClassSPIChart from './StudentVsClassSPIChart';
import TopicWisePerformanceChart from './TopicWisePerformanceChart';
import StudentClassHeatmaps from './StudentClassHeatmaps';
import manyuLogo from '../assets/manyu_navy_blue.png';
import ternLogo from '../assets/Tern_logo_inverted_with_text.png';
import manyuWLogo from '../assets/manyu_white.png';
let current_subject;
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
      "Physical Chemistry (PUC-I)": [
          "Some Basic Concepts of Chemistry (PUC-I)",
          "Structure of Atom (PUC-I)",
          "Thermodynamics (PUC-I)",
          "Equilibrium (PUC-I)",
          "Redox Reactions (PUC-I)",
      ],
      "Physical Chemistry (PUC-II)":[
        "Solutions (PUC-II)",
        "Electrochemistry (PUC-II)",
        "Chemical Kinetics (PUC-II)"
      ],
      "Inorganic Chemistry (PUC-I)": [
          "Classification of Elements and Periodicity in Properties (PUC-I)",
          "Chemical Bonding and Molecular Structure (PUC-I)",
      ],
      "Inorganic Chemistry (PUC-II)": [
          "The d and f Block Elements (PUC-II)",
          "Coordination Compounds (PUC-II)"
      ],
      "Organic Chemistry(PUC-I)": [
          "Organic Chemistry: Some Basic Principles and Techniques (PUC-I)",
          "Hydrocarbons (PUC-I)",
      ],
      "Organic Chemistry(PUC-II)": [
          "Haloalkanes and Haloarenes (PUC-II)",
          "Alcohols, Phenols and Ethers (PUC-II)",
          "Aldehydes, Ketones and Carboxylic Acids (PUC-II)",
          "Amines (PUC-II)",
          "Biomolecules (PUC-II)"
      ],
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

const today = new Date();
const formattedDate = today.getDate().toString().padStart(2, '0') + '/' + 
                      (today.getMonth() + 1).toString().padStart(2, '0') + '/' + 
                      today.getFullYear();

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
          const date_of_test=testKey.split('-')[0];
          groupedScores[block][date_of_test] = count > 0 ? Math.round(totalScore / count) : null;
        }
      }
    }
  });

  return groupedScores;
};


const HomePage = ({ studentData, classData, studentInfo }) => {
  if (!studentData || !classData) {
    return <div className="text-center text-gray-500">Loading data...</div>;
  }

  const studentSPI = studentData[studentData.length - 1][Object.keys(studentData[studentData.length - 1])[0]].Avg_SPI_till_date;
  const classSPI = classData[classData.length - 1][Object.keys(classData[classData.length - 1])[0]].Avg_SPI_of_class_till_date;
  current_subject=studentInfo["subject"];
  const studentTopicData = groupByBlocks(studentData, 'student');
  const classTopicData = groupByBlocks(classData, 'class');


  return (
    <div className="max-w mx-auto">
      <div className="bg-white overflow-hidden relative">
        {/* Header with logo and university name */}
        <div className="text-white p-8 flex items-center justify-center" style={{ backgroundColor: 'rgba(5, 5, 53, 1)' }}>
           <div className="flex items-center">
                      <div className="mr-4">
                        <img src={manyuWLogo} alt="Institute Logo" className="h-30" />
                      </div>
                    </div>
        </div>

        {/* Report Card Title */}
        <div className="bg-cream-50 py-8">
            <h1 className="text-5xl font-bold text-center" style={{ color: 'rgba(5, 5, 53, 1)' }}>
              REPORT CARD
            </h1>
            <div className="mt-6 mx-auto w-full max-w-screen-xl" style={{ borderTop: '2px solid rgba(5, 5, 53, 0.5)' }}></div>
          </div>

          {/* Student Information */}
          <div className="bg-cream-50 px-12 p-12">
            <div className="grid grid-cols-2 gap-16 mb-12">
              <div className="space-y-6">
                <div>
                  <span className="text-2xl font-bold">Student Name:</span>
                  <span className="text-2xl ml-2">{studentInfo.name}</span>
                </div>
                <div>
                  <span className="text-2xl font-bold">Roll No:</span>
                  <span className="text-2xl ml-2">{studentInfo.studentNo}</span>
                </div>
                <div>
                  <span className="text-2xl font-bold">Generated On:</span>
                  <span className="text-2xl ml-2">{formattedDate}</span>
                </div>
              </div>
              <div className="space-y-6">
                <div className="text-right text-gray-800 flex flex-col items-center justify-center">
                  <div className="text-6xl font-bold">{studentInfo.rank} <span className="text-4xl">/{studentInfo.total_students}</span></div>
                  <div className="text-sm text-gray-600 mt-2">Rank Achieved in Latest Test</div>
                </div>
              </div>
            </div>
            <div className="mt-6 mx-auto w-full max-w-screen-xl" style={{ borderTop: '2px solid rgba(5, 5, 53, 0.5)' }}></div>

                    

          {/* Charts Section */}
          <div className="space-y-8">
            {/* First Row: 2 charts side by side */}
            <div className="grid grid-cols-1 lg:grid-cols-2 gap-8 justify-center shadow-md rounded-lg p-4">
                <StudentVsClassAvgChart studentData={studentData} classData={classData} />
                <TopicWisePerformanceChart studentData={studentTopicData} classData={classTopicData}/>
            </div>
            
            {/* Second Row: Heatmap (full width) */}
            <div className="bg-white p-4 rounded-lg shadow-md">
              <StudentClassHeatmaps studentData={studentTopicData} classData={classTopicData} />
            </div>
                        
            {/* Third Row: SPI Chart (full width) */}
            <div className="bg-white p-6 rounded-lg shadow-md">
              <StudentVsClassSPIChart studentSPI={studentSPI} classSPI={classSPI} />
            </div>
          </div>
        </div>

        {/* Bottom section with logos */}
        <div className="bg-cream-50 p-8 flex justify-between items-center">
          {/* Your company logo */}
          <div className="flex items-center">
            <img 
              src={manyuLogo}
              alt="Institute Logo" 
              className="h-25 w-auto mr-2 pl-5"
            />
          </div>
          
          {/* Institute logo */}
          <div>
            <img 
              src={ternLogo}
              alt="Tern Logo" 
              className="h-40 w-auto"
            />
          </div>
        </div>

        {/* Bottom border decoration with branding */}
        <div className="h-12 relative flex items-center justify-center" style={{ backgroundColor: 'rgba(5, 5, 53, 1)' }}>
          <div className="text-lg text-white" >
            made with ❤️ by Tern
          </div>
        </div>
      </div>
    </div>
  );
};

export default HomePage;
import React from 'react';
import StudentVsClassAvgChart from './components/StudentVsClassAvgChart';
import StudentVsClassSPIChart from './components/StudentVsClassSPIChart';
import TopicWisePerformanceChart from './components/TopicWisePerformanceChart';
import StudentClassHeatmaps from './components/StudentClassHeatmaps';
// Import JSON data
import studentData from './Data/242007.json';
import classData from './Data/common_data.json';

const subjects = {
  PHYSICS: {
    Mechanics: [
      "Units and Measurements (PUC-I)", "Motion in a Straight Line (PUC-I)", "Motion in a Plane (PUC-I)", 
      "Laws of Motion (PUC-I)", "Work, Energy and Power (PUC-I)", "System of Particles and Rotational Motion (PUC-I)",
      "Gravitation (PUC-I)", "Mechanical Properties of Solids (PUC-I)", "Mechanical Properties of Fluids (PUC-I)"
    ],
    "Thermodynamics and Kinetic Theory": ["Thermal Properties of Matter (PUC-I)", "Thermodynamics (PUC-I)", "Kinetic Theory (PUC-I)"],
    "Waves and Oscillations": ["Oscillations (PUC-I)", "Waves (PUC-I)"],
    "Electricity and Magnetism": ["Electric Charges and Fields (PUC-II)", "Electrostatic Potential and Capacitance (PUC-II)", 
      "Current Electricity (PUC-II)", "Moving Charges and Magnetism (PUC-II)", "Magnetism and Matter (PUC-II)",
      "Electromagnetic Induction (PUC-II)", "Alternating Current (PUC-II)"],
    Optics: ["Electromagnetic Waves (PUC-II)", "Ray Optics and Optical Instruments (PUC-II)", "Wave Optics (PUC-II)"],
    "Modern Physics": ["Dual Nature of Radiation and Matter (PUC-II)", "Atoms (PUC-II)", "Nuclei (PUC-II)", 
      "Semiconductor Electronics Materials, Devices and Simple Circuits (PUC-II)"]
  },
  CHEMISTRY: {
    "Physical Chemistry": ["Some Basic Concepts of Chemistry (PUC-I)", "Structure of Atom (PUC-I)", "Classification of Elements and Periodicity in Properties (PUC-I)",
      "Chemical Bonding and Molecular Structure (PUC-I)", "Thermodynamics (PUC-I)", "Equilibrium (PUC-I)", "Redox Reactions (PUC-I)",
      "Solutions (PUC-II)", "Electrochemistry (PUC-II)", "Chemical Kinetics (PUC-II)"],
    "Inorganic Chemistry": ["The d and f Block Elements (PUC-II)", "Coordination Compounds (PUC-II)"],
    "Organic Chemistry": ["Organic Chemistry: Some Basic Principles and Techniques (PUC-I)", "Hydrocarbons (PUC-I)", 
      "Haloalkanes and Haloarenes (PUC-II)", "Alcohols, Phenols and Ethers (PUC-II)", "Aldehydes, Ketones and Carboxylic Acids (PUC-II)",
      "Amines (PUC-II)", "Biomolecules (PUC-II)"]
  },
  MATHEMATICS: {
    Algebra: ["Sets (PUC-I)", "Relations and Functions (PUC-I)", "Complex Numbers and Quadratic Equations (PUC-I)",
      "Linear Inequalities (PUC-I)", "Permutations and Combinations (PUC-I)", "Binomial Theorem (PUC-I)",
      "Sequences and Series (PUC-I)", "Matrices (PUC-II)", "Determinants (PUC-II)"],
    Trigonometry: ["Trigonometric Functions (PUC-I)", "Inverse Trigonometric Functions (PUC-II)"],
    "Coordinate Geometry": ["Straight Lines (PUC-I)", "Conic Sections (PUC-I)", "Introduction to Three Dimensional Geometry (PUC-I)",
      "Three Dimensional Geometry (PUC-II)"],
    Calculus: ["Limits and Derivatives (PUC-I)", "Continuity and Differentiability (PUC-II)", "Application of Derivatives (PUC-II)",
      "Integrals (PUC-II)", "Application of Integrals (PUC-II)", "Differential Equations (PUC-II)"],
    "Statistics and Probability": ["Statistics (PUC-I)", "Probability (PUC-I)", "Probability (PUC-II)"],
    "Linear Programming": ["Linear Programming (PUC-II)"],
    "Vector Algebra": ["Vector Algebra (PUC-II)"]
  }
};

// Function to group chapter data into blocks
const groupByBlocks = (data, type) => {
  const groupedScores = {};
  const lastTest = data[data.length - 1];
  const testKey = Object.keys(lastTest)[0];
  const testData = lastTest[testKey][`Avg_of_${type}_chapter_wise`];

  for (const subject in subjects) {
    for (const block in subjects[subject]) {
      const chapters = subjects[subject][block];
      let totalScore = 0, count = 0;

      chapters.forEach((chapter) => {
        if (testData[chapter] !== undefined) {
          totalScore += testData[chapter];
          count++;
        }
      });

      if (count > 0) {
        groupedScores[block] = totalScore / count; // Average score per block
      }
    }
  }

  return groupedScores;
};

const App = () => {
  if (!studentData || !classData) {
    return <div className="text-center text-gray-500">Loading data...</div>;
  }

  const studentSPI = studentData[studentData.length - 1][Object.keys(studentData[studentData.length - 1])[0]].Avg_SPI_till_date;
  const classSPI = classData[classData.length - 1][Object.keys(classData[classData.length - 1])[0]].Avg_SPI_of_class_till_date;

  const studentTopicData = groupByBlocks(studentData, 'student');
  const classTopicData = groupByBlocks(classData, 'class');

  return (
    <div className="p-4 space-y-6">
      <StudentVsClassAvgChart studentData={studentData} classData={classData} />
      <StudentVsClassSPIChart studentSPI={studentSPI} classSPI={classSPI} />
      <TopicWisePerformanceChart studentData={studentTopicData} classData={classTopicData} />
      <StudentClassHeatmaps studentData={studentData} classData={classData} />
    </div>
  );
};

export default App;

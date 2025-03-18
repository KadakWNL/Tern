import React from 'react';

const ReportCard = () => {
  // Sample student data - this would normally come from props or an API
  const studentInfo = {
    name: "Shreyas",
    studentNo: "69",
    yearLevel: "1",
    course: "How to get bitches",
    major: "wiffing",
    term: "2 years"
  };
  
  // Your software name
  const softwareName = "Test";

  return (
    <div className="max-w-5xl mx-auto p-6">
      <div className="bg-white rounded-lg shadow-lg overflow-hidden relative">
        {/* Header with logo and university name */}
        <div className="bg-blue-800 text-white p-8 flex items-center justify-center">
          <div className="flex items-center">
            <div className="mr-6">
              <div className="w-24 h-24 relative">
                <div className="absolute inset-0 border-4 border-white rounded-full flex items-center justify-center">
                  <span className="text-4xl font-bold">M</span>
                </div>
                <div className="absolute inset-0 border-4 border-white rounded-full" style={{
                  borderLeftColor: 'transparent',
                  borderBottomColor: 'transparent',
                  transform: 'rotate(45deg)'
                }}></div>
              </div>
            </div>
            <div>
              <h1 className="text-3xl font-bold">Manyu Classes</h1>
              {/* <h2 className="text-2xl">UNIVERSITY</h2> */}
            </div>
          </div>
        </div>

        {/* Report Card Title */}
        <div className="bg-cream-50 py-8">
          <h1 className="text-5xl font-bold text-blue-800 text-center">REPORT CARD</h1>
          <div className="mt-6 border-t-2 border-blue-800 mx-24"></div>
        </div>

        {/* Student Information */}
        <div className="bg-cream-50 p-12 grid grid-cols-2 gap-16">
          <div className="space-y-6">
            <div>
              <span className="text-2xl font-bold">Student Name:</span>
              <span className="text-2xl ml-2">{studentInfo.name}</span>
            </div>
            <div>
              <span className="text-2xl font-bold">Student No.:</span>
              <span className="text-2xl ml-2">{studentInfo.studentNo}</span>
            </div>
            <div>
              <span className="text-2xl font-bold">Year Level:</span>
              <span className="text-2xl ml-2">{studentInfo.yearLevel}</span>
            </div>
          </div>
          <div className="space-y-6">
            <div>
              <span className="text-2xl font-bold">Course:</span>
              <span className="text-2xl ml-2">{studentInfo.course}</span>
            </div>
            <div>
              <span className="text-2xl font-bold">Major:</span>
              <span className="text-2xl ml-2">{studentInfo.major}</span>
            </div>
            <div>
              <span className="text-2xl font-bold">Term:</span>
              <span className="text-2xl ml-2">{studentInfo.term}</span>
            </div>
          </div>
        </div>

        {/* Bottom section with logos */}
        <div className="bg-cream-50 p-8 flex justify-between items-center">
          {/* Your company logo */}
          <div className="flex items-center">
            <img 
              src="/api/placeholder/120/60" 
              alt="Institute Logo" 
              className="h-16 w-auto mr-2"
            />
          </div>
          
          {/* Institute logo */}
          <div>
            <img 
              src="/api/placeholder/120/60" 
              alt="Tern Logo" 
              className="h-16 w-auto"
            />
          </div>
        </div>

        {/* Bottom border decoration with branding */}
        <div className="h-12 bg-blue-800 relative flex items-center justify-center">
          <div className="text-white text-lg">
            made with ❤️ by Tern
          </div>
        </div>
      </div>
    </div>
  );
};

const App = () => {
  return (
    <div className="min-h-screen bg-gray-100 py-12">
      <ReportCard />
    </div>
  );
};

export default App;
// src/ReportCard.jsx

import React from 'react';
import student_performance_over_time from "./assets/student_performance_over_time.png";
import student_vs_class_heatmaps from "./assets/student_vs_class_heatmaps.png"
import student_vs_class_spi from "./assets/student_vs_class_spi.png"

const ReportCard = () => {
    return (
        <div className="w-11/12 max-w-5xl mx-auto bg-white shadow-2xl rounded-2xl overflow-hidden my-10">
            {/* Header */}
            <div className="bg-blue-600 p-6 text-white text-center">
                <h1 className="text-4xl font-bold">Name of Institution</h1>
                <h2 className="text-2xl">Student Assessment</h2>
            </div>

            <div className="p-8">
                {/* Student Info */}
                <div className="grid grid-cols-2 gap-4 text-lg">
                    <div>
                        <p><strong>Student Name:</strong> Name</p>
                        <br></br>
                        <p><strong>Roll No:</strong> 242007</p>
                    </div>
                    <div>
                        <p> <br></br></p>
                        <p><strong>Current SPI:</strong> 69</p>
                        <p><br></br> </p>
                    </div>
                </div>

                <div className="mt-8">
                    <h3 className="font-bold text-2xl text-center">Performance Analysis</h3>

                    <div className="mt-4 flex flex-col gap-10">
                        {/* Image 1 - Stretched, No Clipping */}
                        <img src={student_performance_over_time} 
                            alt="Time Graph" 
                            className="w-full h-[30vh] object-cover rounded-lg"/>

                        {/* Image 2 - Stretched, No Clipping */}
                        <img src={student_vs_class_heatmaps} 
                            alt="Heatmap Graph" 
                            className="w-full h-[35vh] object-cover rounded-lg"/>

                        {/* Image 3 - Stretched, No Clipping */}
                        <img src={student_vs_class_spi} 
                            alt="Subject Analysis Graph" 
                            className="w-full h-[40vh] object-cover rounded-lg"/>
                    </div>
                </div>



                {/* GPA Scale */}
                <div className="mt-8">
                    <h3 className="font-bold text-2xl">GPA Grade Scale</h3>
                    <table className="w-full mt-4 border-collapse text-lg">
                        <tbody>
                            {[
                                ["1.00 = 97-100", "2.50 = 74-77"],
                                ["1.25 = 93-96", "2.75 = 71-73"],
                                ["1.50 = 89-92", "3.00 = 60-70"]
                            ].map((row, i) => (
                                <tr key={i} className="border-b bg-gray-100">
                                    {row.map((grade, j) => (
                                        <td key={j} className="py-4 px-6 text-center">{grade}</td>
                                    ))}
                                </tr>
                            ))}
                        </tbody>
                    </table>
                </div>
            </div>
        </div>
    );
};

export default ReportCard;

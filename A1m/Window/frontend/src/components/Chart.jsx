import Chart from 'react-apexcharts';
import React, { useRef } from 'react';

export default function AllGraphs() {

  const lineRef = useRef(null);
  const barRef = useRef(null);
  const heatmapRef = useRef(null);
  const radarRef = useRef(null);

  const downloadGraph = (chartRef, filename) => {
    if (chartRef.current && chartRef.current.chart) {
      chartRef.current.chart.dataURI().then(({ imgURI }) => {
        const link = document.createElement('a');
        link.href = imgURI;
        link.download = `${filename}.png`;
        link.click();
      });
    }
  };

  // ✅ LINE CHART DATA
  const lineData = {
    series: [{
      name: 'Performance',
      data: [80, 85, 70, 90, 60, 75]
    }],
    options: {
      chart: { type: 'line', toolbar: { show: false } },
      xaxis: { categories: ['Math', 'Physics', 'Chemistry', 'Bio', 'CS', 'English'] },
      colors: ['#FF5733'],
      dataLabels: { enabled: true }
    }
  };

  // ✅ BAR CHART DATA
  const barData = {
    series: [{
      name: 'Marks',
      data: [95, 82, 78, 89, 76, 84]
    }],
    options: {
      chart: { type: 'bar', toolbar: { show: false } },
      xaxis: { categories: ['Math', 'Physics', 'Chemistry', 'Bio', 'CS', 'English'] },
      colors: ['#34D399'],
      dataLabels: { enabled: true }
    }
  };

  // ✅ HEATMAP DATA
  const heatmapData = {
    series: [
      { name: 'Math', data: [90, 85, 88, 70, 60, 80] },
      { name: 'Physics', data: [60, 78, 85, 90, 65, 80] },
      { name: 'Chemistry', data: [80, 85, 70, 95, 75, 88] }
    ],
    options: {
      chart: { type: 'heatmap', toolbar: { show: false } },
      dataLabels: { enabled: true },
      colors: ['#008FFB']
    }
  };

  // ✅ RADAR CHART DATA
  const radarData = {
    series: [{
      name: 'Score',
      data: [80, 85, 90, 70, 75, 60]
    }],
    options: {
      chart: { type: 'radar', toolbar: { show: false } },
      xaxis: { categories: ['Math', 'Physics', 'Chemistry', 'Bio', 'CS', 'English'] },
      colors: ['#FF4560']
    }
  };

  return (
    <div className="grid grid-cols-2 gap-4 p-4">

      {/* Line Chart */}
      <div className="bg-white p-4 rounded-lg shadow-md">
        <h2 className="text-xl font-bold mb-2">Line Chart</h2>
        <Chart ref={lineRef} options={lineData.options} series={lineData.series} type="line" height={250} />
        <button onClick={() => downloadGraph(lineRef, 'line_chart')} className="mt-2 text-blue-500">Download</button>
      </div>

      {/* Bar Chart */}
      <div className="bg-white p-4 rounded-lg shadow-md">
        <h2 className="text-xl font-bold mb-2">Bar Chart</h2>
        <Chart ref={barRef} options={barData.options} series={barData.series} type="bar" height={250} />
        <button onClick={() => downloadGraph(barRef, 'bar_chart')} className="mt-2 text-blue-500">Download</button>
      </div>

      {/* Heatmap Chart */}
      <div className="bg-white p-4 rounded-lg shadow-md">
        <h2 className="text-xl font-bold mb-2">Heatmap Chart</h2>
        <Chart ref={heatmapRef} options={heatmapData.options} series={heatmapData.series} type="heatmap" height={250} />
        <button onClick={() => downloadGraph(heatmapRef, 'heatmap_chart')} className="mt-2 text-blue-500">Download</button>
      </div>

      {/* Radar Chart */}
      <div className="bg-white p-4 rounded-lg shadow-md">
        <h2 className="text-xl font-bold mb-2">Radar Chart</h2>
        <Chart ref={radarRef} options={radarData.options} series={radarData.series} type="radar" height={250} />
        <button onClick={() => downloadGraph(radarRef, 'radar_chart')} className="mt-2 text-blue-500">Download</button>
      </div>

    </div>
  );
}
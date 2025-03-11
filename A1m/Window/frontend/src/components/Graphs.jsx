import ApexCharts from 'apexcharts';

// ========================
// ✅ File Paths & Data
// ========================
const dataPath = '../../../../../Data/Processed/PHYSICS/242007.json';
const commonDataPath = '../../../../../Data/Processed/PHYSICS/common_data.json';
const rollNumber = 242007;
const subject = "PHYSICS";


async function fetchData() {
    const studentData = await fetch(dataPath).then(res => res.json());
    const commonData = await fetch(commonDataPath).then(res => res.json());

    createLineChart(studentData, commonData);
    createBarChart(studentData, commonData);
    createRadarChart(studentData, commonData);
    createHeatmapChart(studentData, commonData);
}

function createLineChart(studentData, commonData) {
    const dates = studentData.map(test => Object.keys(test)[0]);
    const studentAvg = studentData.map(test => Object.values(test)[0]['Avg_of_test']);
    const classAvg = commonData.map(test => Object.values(test)[0]['Avg_of_class']);

    const options = {
        chart: {
            type: 'line',
        },
        series: [
            {
                name: 'Student Average',
                data: studentAvg
            },
            {
                name: 'Class Average',
                data: classAvg
            }
        ],
        xaxis: {
            categories: dates
        }
    };

    const chart = new ApexCharts(document.querySelector("#lineChart"), options);
    chart.render();
}

function createBarChart(studentData, commonData) {
    const lastStudentTest = Object.values(studentData[studentData.length-1])[0];
    const lastClassTest = Object.values(commonData[commonData.length-1])[0];

    const studentSPI = lastStudentTest['Avg_SPI_till_date'];
    const classSPI = lastClassTest['Avg_SPI_of_class_till_date'];

    const options = {
        chart: {
            type: 'bar'
        },
        series: [{
            data: [classSPI, studentSPI]
        }],
        xaxis: {
            categories: ['Class SPI', 'Student SPI']
        }
    };

    const chart = new ApexCharts(document.querySelector("#barChart"), options);
    chart.render();
}

function createRadarChart(studentData, commonData) {
    const lastStudentTest = Object.values(studentData[studentData.length-1])[0]['Avg_of_student_chapter_wise'];

    const categories = Object.keys(lastStudentTest);
    const values = Object.values(lastStudentTest);

    const options = {
        chart: {
            type: 'radar'
        },
        series: [{
            name: 'Student Performance',
            data: values
        }],
        xaxis: {
            categories: categories
        }
    };

    const chart = new ApexCharts(document.querySelector("#radarChart"), options);
    chart.render();
}

function createHeatmapChart(studentData, commonData) {
    const heatmapData = [];

    studentData.forEach(test => {
        const testName = Object.keys(test)[0];
        const testScores = Object.values(test)[0]['Avg_of_student_chapter_wise'];

        Object.keys(testScores).forEach(topic => {
            heatmapData.push({
                x: testName,
                y: topic,
                z: testScores[topic]
            });
        });
    });

    const options = {
        chart: {
            type: 'heatmap'
        },
        series: [{
            name: 'Scores',
            data: heatmapData
        }]
    };

    const chart = new ApexCharts(document.querySelector("#heatmapChart"), options);
    chart.render();
}

fetchData();

// Create a dashboard layout
const appContainer = document.querySelector("#app");
appContainer.innerHTML = `
    <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 20px;">
        <div><h3>Performance Over Time</h3><div id="lineChart"></div></div>
        <div><h3>Class SPI vs Student SPI</h3><div id="barChart"></div></div>
        <div><h3>Topic-Wise Performance</h3><div id="radarChart"></div></div>
        <div><h3>Performance Heatmap</h3><div id="heatmapChart"></div></div>
    </div>
`;
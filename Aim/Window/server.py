from fastapi import FastAPI
from fastapi.responses import JSONResponse, FileResponse
from fastapi.middleware.cors import CORSMiddleware
import os
import asyncio
from playwright.async_api import async_playwright  # Playwright import

app = FastAPI()

# Enable CORS for frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # Allow frontend origin
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# API Endpoint for sample data
@app.get("/api/data")
def get_data():
    return JSONResponse({
        "student_name": "Test_name",
        "date": "05/01/2025",
        "roll_number": 242007,
        "subject": "PHYSICS"
    })



# Add a specific function to handle chart conversion
async def convert_charts_to_images(page):
    await page.evaluate("""
    // Create a function that returns a promise for chart readiness
    function waitForCharts() {
        return new Promise(resolve => {
            const checkCharts = () => {
                const charts = document.querySelectorAll('.apexcharts-canvas');
                let allReady = true;
                charts.forEach(chart => {
                    if (!chart.querySelector('svg') || 
                        chart.getBoundingClientRect().width === 0) {
                        allReady = false;
                    }
                });
                
                if (allReady && charts.length > 0) {
                    resolve();
                } else {
                    setTimeout(checkCharts, 100);
                }
            };
            checkCharts();
        });
    }
    
    // Call the function but don't use await inside evaluate
    return waitForCharts().then(() => {
        // Convert to static images with proper dimensions
        document.querySelectorAll('.apexcharts-canvas').forEach(chart => {
            const svg = chart.querySelector('svg');
            if (svg) {
                // Get computed dimensions
                const rect = chart.getBoundingClientRect();
                const width = rect.width;
                const height = rect.height;
                
                // Create new image
                const img = document.createElement('img');
                const serializer = new XMLSerializer();
                const svgString = serializer.serializeToString(svg);
                const svgBase64 = "data:image/svg+xml;base64," + btoa(unescape(encodeURIComponent(svgString)));
                
                img.src = svgBase64;
                img.style.width = width + 'px';
                img.style.height = height + 'px';
                img.style.display = 'block'; // Important for layout
                
                // Replace with image while preserving container dimensions
                const container = chart.parentElement;
                container.style.width = width + 'px';
                container.style.height = height + 'px';
                container.style.display = 'inline-block'; // Keep side by side layout
                chart.replaceWith(img);
            }
        });
        return true;
    });
    """)
# Playwright function to generate PDF
async def create_pdf():
    pdf_path = "output.pdf"

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page(viewport={"width": 1200, "height": 1600})

        await page.goto("http://127.0.0.1:8000/bwreport", wait_until="networkidle")
        await page.wait_for_selector(".apexcharts-canvas", timeout=10000)
        await asyncio.sleep(3)  # Give charts time to fully render
        
        # Force window resize
        await page.evaluate("window.dispatchEvent(new Event('resize'))")
        await asyncio.sleep(1)
        
        # Add CSS that helps maintain layout
        await page.add_style_tag(content="""
    .charts-row, .row {
        display: flex !important;
        flex-wrap: wrap !important;  /* Allow items to wrap */
        justify-content: center !important; /* Center items */
    }
    
    .apexcharts-canvas {
        max-width: 100% !important; /* Ensure charts don't exceed container width */
        overflow: hidden !important;
    }
""")
    
        
        await asyncio.sleep(1)
        
        # Generate PDF
        await page.pdf(
            path=pdf_path,
            format="A4",
            print_background=True,
            scale=0.75
        )

        await browser.close()
        print("✅ PDF generated successfully!")

    return pdf_path
# FastAPI endpoint to trigger PDF generation
@app.get("/d")
async def generate_pdf():
    pdf_file = await create_pdf()
    return FileResponse(pdf_file, filename="exported_page.pdf", media_type="application/pdf")

# Serve React Frontend
@app.get("/{full_path:path}")  # Handles all routes (Fixes 404 errors)
def serve_react(full_path: str = ""):
    react_build_path = os.path.join(os.path.dirname(__file__), "frontend", "dist")

    # Serve index.html for any path
    index_file = os.path.join(react_build_path, "index.html")
    file_path = os.path.join(react_build_path, full_path)

    if os.path.exists(file_path) and os.path.isfile(file_path):
        return FileResponse(file_path)  # Serve actual file (JS, CSS, etc.)
    
    if os.path.exists(index_file):
        return FileResponse(index_file)  # Serve React index.html
    
    return JSONResponse({"error": "React build not found"}, status_code=404)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)

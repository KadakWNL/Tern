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

# Playwright function to generate PDF
async def create_pdf():
    pdf_path = "output.pdf"

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)  # Runs without UI
        page = await browser.new_page()

        # Load the frontend page
        await page.goto("http://localhost:5173", wait_until="networkidle")

        # Wait for the page body to ensure full load
        await page.wait_for_selector("body", timeout=20000)  # 20 sec timeout

        # Extra delay to allow full rendering
        await asyncio.sleep(3)  # Wait 3 seconds before capturing the PDF

        # Adjust body style for better PDF layout
        await page.evaluate("""
            document.body.style.width = '100%';  // Full width
            document.body.style.height = '1123px';  // A4 height in pixels (portrait)
            document.body.style.margin = '0';  // Remove margin
            document.body.style.padding = '0';  // Remove padding
            document.body.style.overflow = 'hidden';  // Prevent page breaks
        """)
        
        # Ensure graphs are handled correctly for printing
        await page.evaluate("""
            let graphs = document.querySelectorAll('.graph-container');
            graphs.forEach(graph => {
                graph.style.display = 'inline-block';
                graph.style.width = '45%'; // Adjust to fit side by side
                graph.style.height = 'auto'; // Ensure graphs don't overflow
            });
        """)

        # Generate PDF and save it
        await page.pdf(
            path=pdf_path, 
            format="A4", 
            print_background=True,
            margin={"top": "10px", "bottom": "10px", "left": "10px", "right": "10px"},
            scale=0.8,  # Adjust scale to fit content within a single page
            height="1123px",  # Explicitly set height to A4 height
            width="794px"  # Explicitly set width to A4 width
        )  

        await browser.close()
        print("✅ PDF generated successfully!")

    return pdf_path

# FastAPI endpoint to trigger PDF generation
@app.get("/generate-pdf")
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

from fastapi import FastAPI
from fastapi.responses import JSONResponse, FileResponse
from fastapi.middleware.cors import CORSMiddleware
import os

app = FastAPI()

# Enable CORS for frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # Allow frontend origin
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# API Endpoint
@app.get("/api/data")
def get_data():
    return JSONResponse({
        "student_name": "Test_name",
        "date":r"05/01/2025",
        "roll_number" : 242007,
        "subject" : "PHYSICS"
        
    })

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

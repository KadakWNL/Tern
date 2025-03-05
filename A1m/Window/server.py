from fastapi import FastAPI
from fastapi.responses import JSONResponse
import os

app = FastAPI()

# Sample data (replace with real data from your program)
@app.get("/api/data")
def get_data():
    return JSONResponse({
        "student_name": "Test_name",
        "roll_no": "242007",
        "metrics": {
            "SPI": 89.5,
            "Attendance": "95%",
            "Rank": 5
        }
    })

# Serve the React frontend
@app.get("/")
def serve_react():
    index_path = os.path.join("frontend", "dist", "index.html")
    if os.path.exists(index_path):
        with open(index_path, "r") as file:
            return file.read()
    return JSONResponse({"error": "React build not found"}, status_code=404)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)

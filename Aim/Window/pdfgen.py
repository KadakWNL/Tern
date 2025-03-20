import plotly.express as px
import pandas as pd
import plotly.io as pio
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from svglib.svglib import svg2rlg
from reportlab.graphics.renderPDF import drawToFile

# 📌 Step 1: Create DataFrame from the provided data
data = {
    "Category": [
        "Mechanics", "Thermodynamics and Kinetic Theory", "Waves and Oscillations",
        "Electricity and Magnetism", "Optics", "Modern Physics"
    ],
    "PHYSICS-101": [15, 33, 30, 14, 0, 25],
    "PHYSICS-102": [29, 17, 15, 19, 24, 50],
}

df = pd.DataFrame(data)

# 📌 Step 2: Convert DataFrame to Long Format for Heatmap
df_long = df.melt(id_vars=["Category"], var_name="Course", value_name="Score")

# 📌 Step 3: Create a Heatmap using Plotly
fig = px.density_heatmap(df_long, x="Course", y="Category", z="Score", 
                         color_continuous_scale="Blues", title="Physics Performance Heatmap")

# 📌 Step 4: Save Heatmap as SVG
svg_path = "heatmap.svg"
pio.write_image(fig, svg_path)

# 📌 Step 5: Convert SVG to PDF
pdf_path = "heatmap.pdf"
drawing = svg2rlg(svg_path)
drawToFile(drawing, pdf_path)

print(f"✅ Heatmap saved as {pdf_path}")

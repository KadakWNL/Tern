import tkinter as tk
from tkinter import Toplevel
from PIL import Image, ImageTk

roll_no = '242007'
name_of_student = 'Test_name'

def open_graph_window(parent):
    new_win = Toplevel(parent)
    new_win.title("Graphs and Data")
    new_win.geometry("600x500")  # Adjust as needed
    new_win.configure(bg='white')

    # Create a frame for grid layout
    frame = tk.Frame(new_win, bg="white")
    frame.pack(fill="both", expand=True, padx=10, pady=10)

    # Load images
    img1 = Image.open(r"Data\Graph\student_vs_class_heatmaps.png").resize((250, 250))
    img1 = ImageTk.PhotoImage(img1)

    img2 = Image.open(r"Data\Graph\student_vs_class_heatmaps.png").resize((250, 250))
    img2 = ImageTk.PhotoImage(img2)

    # Student Details
    name_label = tk.Label(frame, text=f'Name of the student: {name_of_student}.', bg="white", font=("Arial", 12))
    roll_label = tk.Label(frame, text=f'Roll number of the student: {roll_no}.', bg="white", font=("Arial", 12))

    # Image Labels
    label1 = tk.Label(frame, image=img1, bg="white")
    label1.image = img1  # Keep reference

    label2 = tk.Label(frame, image=img2, bg="white")
    label2.image = img2  # Keep reference

    # Text Data
    text_label = tk.Label(frame, text="Some important data:\n- Value 1: 123\n- Value 2: 456", 
                          font=("Arial", 12), bg="white")

    # Grid Placement
    name_label.grid(row=0, column=0, sticky="w", padx=10, pady=(10, 2))  # Top-left
    roll_label.grid(row=1, column=0, sticky="w", padx=10, pady=(0, 10))  # Below name, aligned left

    label1.grid(row=2, column=0, padx=10, pady=10, columnspan=2)  # Centered image
    label2.grid(row=2, column=1, padx=10, pady=10)  # Centered image

    text_label.grid(row=3, column=0, columnspan=2, pady=10)  # Full width below graphs

    # Adjust column weights
    frame.columnconfigure(0, weight=1)
    frame.columnconfigure(1, weight=1)


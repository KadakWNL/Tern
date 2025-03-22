import concurrent.futures
import threading
import webbrowser
import requests
from backend import shared_state
import json
import pandas as pd
import tkinter as tk
import customtkinter as ctk
from CTkMessagebox import CTkMessagebox

# Use your theme colors
THEME_COLORS = {
    "navbar_bg": "#050535",      
    "navbar_text": "white", 
    "main_bg": "white",      
    "main_text": "black",         
    "button_bg": "#050535",       
    "button_text": "white",       
    "hover_color": "#08086b"      
}

def check_data(roll, subject):
    path = rf"Data/Processed/{subject}/{roll}.json"
    try:
        with open(path, "r") as file:
            student_data = json.load(file)
        if isinstance(student_data, dict):
            return False
        if len(student_data) > 1:
            return True  
        else:
            return False
    except FileNotFoundError:
        return False

def retrieve_data(roll, student_data_path):
    student_records = pd.read_csv("Data/student_names.csv") 
    student_numbers = list(student_records["Roll Number"])
    student = list(student_records["Name"])[student_numbers.index(int(roll))]
    total_students = len(student_numbers)
    with open(student_data_path, "r") as file:
        student_data = json.load(file)

    try:
        latest_test = student_data[-1] 
    except KeyError:
        latest_test = student_data
    finally:
        latest_test_key = list(latest_test.keys())[0] 
        rank = latest_test[latest_test_key]["Rank"]
        
    return student, rank, total_students

def retrieve_roll_nos():
    data = pd.read_csv("Data/student_names.csv")
    roll_nos = map(lambda x: int(x), list(data["Roll Number"]))
    return list(roll_nos)

def process_student(roll_no, subject, bw, path):
    if not check_data(roll_no, subject):
        return False, f"Skipped roll number {roll_no}"
    
    student_data_path = f"Data/Processed/{subject}/{roll_no}.json"
    
    # Update shared state
    shared_state.update_values(
        new_name=retrieve_data(roll_no, student_data_path)[0],
        new_rollno=roll_no, 
        new_rank=retrieve_data(roll_no, student_data_path)[1],
        new_subject=subject,
        new_total_students=retrieve_data(roll_no, student_data_path)[2]
    )
    
    shared_state.update_path(path)
    
    # Perform download
    try:
        url = "http://127.0.0.1:8000/bwd" if bw else "http://127.0.0.1:8000/d"
        
        # Use a timeout to prevent hanging connections
        response = requests.get(url, stream=True, timeout=30)
        return True, f"Successfully processed roll number {roll_no}"
    except Exception as e:
        return False, f"Error processing roll number {roll_no}: {str(e)}"

def create_progress_window(app, total_count):
    """Create a customtkinter progress window with progress bar"""
    # Create a modal dialog window
    progress_window = ctk.CTkToplevel(app)
    progress_window.title("Download Progress")
    progress_window.geometry("450x220")
    progress_window.resizable(False, False)
    progress_window.configure(fg_color=THEME_COLORS["main_bg"])
    progress_window.iconbitmap(r"Logo\final0.ico")
    # Center the window
    window_width = 450
    window_height = 220
    screen_width = app.winfo_screenwidth()
    screen_height = app.winfo_screenheight()
    x = (screen_width - window_width) // 2
    y = (screen_height - window_height) // 2
    progress_window.geometry(f"{window_width}x{window_height}+{x}+{y}")
    
    # Create the main frame
    frame = ctk.CTkFrame(progress_window, fg_color=THEME_COLORS["main_bg"], corner_radius=10)
    frame.pack(fill=ctk.BOTH, expand=True, padx=20, pady=20)
    
    # Title
    title_label = ctk.CTkLabel(
        frame, 
        text="Downloading PDFs for all students...", 
        font=("Arial", 16, "bold"),
        text_color=THEME_COLORS["main_text"]
    )
    title_label.pack(pady=(0, 15))
    
    # Progress bar
    progress_var = ctk.DoubleVar()
    progress_bar = ctk.CTkProgressBar(
        frame, 
        variable=progress_var,
        width=400,
        height=15,
        corner_radius=5,
        mode="determinate",
        progress_color=THEME_COLORS["button_bg"],
        fg_color="#E0E0E0"
    )
    progress_bar.set(0)
    progress_bar.pack(pady=(0, 15))
    
    # Status message
    status_var = ctk.StringVar(value="Starting downloads...")
    status_label = ctk.CTkLabel(
        frame, 
        textvariable=status_var,
        font=("Arial", 12),
        text_color=THEME_COLORS["main_text"]
    )
    status_label.pack(pady=(0, 10))
    
    # Count label
    count_var = ctk.StringVar(value=f"0/{total_count} complete")
    count_label = ctk.CTkLabel(
        frame, 
        textvariable=count_var,
        font=("Arial", 12, "bold"),
        text_color=THEME_COLORS["button_bg"]
    )
    count_label.pack(pady=(0, 15))
    
    # Make the window modal
    progress_window.transient(app)
    progress_window.grab_set()
    progress_window.focus_set()
    
    return progress_window, progress_var, status_var, count_var

def main(subject, bw, path, app, max_workers=5, buttons_to_disable=None):
    """
    Process all students with parallel execution and progress tracking
    
    Parameters:
    - subject: Subject name
    - bw: Boolean flag for black and white output
    - path: Output path
    - app: The main CustomTkinter window (parent)
    - max_workers: Maximum number of concurrent downloads
    - buttons_to_disable: List of buttons to disable during processing
    """
    roll_numbers = retrieve_roll_nos()
    valid_roll_numbers = [roll for roll in roll_numbers if check_data(roll, subject)]
    total_count = len(valid_roll_numbers)
    
    if total_count == 0:
        return
    
    # Create progress window
    progress_window, progress_var, status_var, count_var = create_progress_window(app, total_count)
    
    # Initialize counters
    completed = 0
    successful = 0
    
    def update_progress(result, roll_no):
        nonlocal completed, successful
        success, message = result
        
        # Update counters
        completed += 1
        if success:
            successful += 1
        
        # Update progress bar and status text
        progress_var.set(completed / total_count)  # CTkProgressBar works with values from 0 to 1
        status_var.set(f"Processing: {message}")
        count_var.set(f"{completed}/{total_count} complete ({successful} successful)")
        
        # Check if all tasks are complete
        if completed >= total_count:
            status_var.set("All downloads complete!")
            
            # Schedule window closure and button re-enabling
            app.after(2000, lambda: close_and_reenable())
    
    def close_and_reenable():
        # Close progress window
        progress_window.grab_release()
        progress_window.destroy()
    
    # Start processing in a separate thread to keep UI responsive
    def run_processing():
        with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
            future_to_roll = {
                executor.submit(process_student, roll_no, subject, bw, path): roll_no 
                for roll_no in valid_roll_numbers
            }
            
            for future in concurrent.futures.as_completed(future_to_roll):
                roll_no = future_to_roll[future]
                try:
                    result = future.result()
                    # Update UI from the main thread
                    app.after(0, lambda r=result, rn=roll_no: update_progress(r, rn))
                except Exception as exc:
                    # Handle exceptions
                    error_result = (False, f"Error with roll {roll_no}: {exc}")
                    app.after(0, lambda r=error_result, rn=roll_no: update_progress(r, rn))
    
    # Start processing thread
    processing_thread = threading.Thread(target=run_processing)
    processing_thread.daemon = True
    processing_thread.start()
    
    # Return the progress window in case caller needs to reference it
    return progress_window


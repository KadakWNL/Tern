import customtkinter as ctk
from tkinter import filedialog, messagebox, PhotoImage
import datetime, file_check, specific_data_main, upload_main, os, csv, json
import work_graph as grph
from datetime import datetime
from CTkTable import *
import threading
import queue
import time
import requests
from ctypes import windll
from PIL import Image
import pandas as pd
from Window import shared_state
from playwright.sync_api import sync_playwright
import os
import webbrowser
import shutil
import asyncio
from playwright.async_api import async_playwright
# Set appearance mode and color theme


THEME_COLORS = {
    "navbar_bg": "#050535",      
    "navbar_text": "white", 
    "main_bg": "white",      
    # "main_bg": "#F2F2F2",           
    "main_text": "black",         
    "button_bg": "#050535",       
    "button_text": "white",       
    "hover_color": "#08086b"      
}

ctk.set_appearance_mode("light")

# Create the main application window
app = ctk.CTk()
app.geometry("900x480")
app.configure(bg="#FFFFFF")
app.title("Tern - Student Progress Tracker")
app.iconbitmap(r"Logo\final_inv.ico")
windll.shell32.SetCurrentProcessExplicitAppUserModelID("tern.mainwindow")
# Grid Configuration for Layout
app.grid_columnconfigure(1, weight=1)  # Right frame expands
app.grid_rowconfigure(0, weight=1)

# Left Frame (Navbar)
frame_left = ctk.CTkFrame(app, width=140, border_width=0, fg_color=THEME_COLORS["navbar_bg"], corner_radius=0)
frame_left.grid(row=0, column=0, sticky="ns")

# Main Content Area (Right Frame)
frame_container = ctk.CTkFrame(app, border_width=0, fg_color="white")
frame_container.grid(row=0, column=1, padx=20, pady=20, sticky="nsew")

# Different Right Frames for Each Page
frame_right_upload = ctk.CTkFrame(frame_container, border_width=0, fg_color=THEME_COLORS["main_bg"])
frame_right_students = ctk.CTkFrame(frame_container, border_width=0, fg_color=THEME_COLORS["main_bg"])
frame_right_download = ctk.CTkFrame(frame_container, border_width=0, fg_color=THEME_COLORS["main_bg"])
frame_right_history = ctk.CTkFrame(frame_container, border_width=0, fg_color=THEME_COLORS["main_bg"])

# Function to Switch Pages
def show_frame(frame):
    # Hide all frames
    for widget in frame_container.winfo_children():
        widget.grid_forget()
    # Show the selected frame
    frame.grid(row=0, column=0, sticky="nsew", padx=5, pady=5)

# Show Dashboard by Default
show_frame(frame_right_upload)

# Navbar Widgets
# Logo placeholder
logo_frame = ctk.CTkFrame(frame_left, width=100, height=100, fg_color="transparent")
logo_frame.pack(pady=(20, 10))

# Create a placeholder for the logo
logo_image = ctk.CTkImage(light_image=Image.open(r"Logo\Tern_logo_with_text.png"), size=(200,200))
logo_label = ctk.CTkLabel(logo_frame, image=logo_image, text="", font=("Arial", 16), 
                          width=80, height=80, fg_color=THEME_COLORS["navbar_bg"], 
                          text_color=THEME_COLORS["navbar_text"])
logo_label.pack(expand=True)

nav_button1 = ctk.CTkButton(frame_left, text="Download", fg_color="transparent", 
                            hover_color=THEME_COLORS["hover_color"],
                            text_color=THEME_COLORS["navbar_text"],
                            command=lambda: show_frame(frame_right_download))
nav_button1.pack(fill="x", pady=5)

nav_button2 = ctk.CTkButton(frame_left, text="Students", fg_color="transparent", 
                            hover_color=THEME_COLORS["hover_color"],
                            text_color=THEME_COLORS["navbar_text"],
                            command=lambda: show_frame(frame_right_students))
nav_button2.pack(fill="x", pady=5)

nav_button3 = ctk.CTkButton(frame_left, text="Upload", fg_color="transparent", 
                            hover_color=THEME_COLORS["hover_color"],
                            text_color=THEME_COLORS["navbar_text"],
                            command=lambda: show_frame(frame_right_upload))
nav_button3.pack(fill="x", pady=5)

nav_button4 = ctk.CTkButton(frame_left, text="History", fg_color="transparent", 
                            hover_color=THEME_COLORS["hover_color"],
                            text_color=THEME_COLORS["navbar_text"],
                            command=lambda: show_frame(frame_right_history))
nav_button4.pack(fill="x", side="bottom", pady=15)

#==============================Test Analysis======================================= 
#==================================================================================
frame_test_analysis_label = ctk.CTkLabel(frame_right_upload, text="Test Analysis", font=("Arial", 24, "bold"),
                                        text_color=THEME_COLORS["main_text"])
frame_test_analysis_label.grid(row=0, column=0, columnspan=4, sticky="ew", pady=10)

#=====================Data and Test Id Entry===================================
#*********************************************************************
date_label = ctk.CTkLabel(frame_right_upload, text="Date(DD/MM/YYYY):", font=("Arial", 18),
                         text_color=THEME_COLORS["main_text"])
date_label.grid(row=1, column=0, padx=20, pady=(20, 10), sticky="w")
date_entry_variable = ctk.StringVar()
date_entry = ctk.CTkEntry(frame_right_upload, placeholder_text="DD/MM/YYYY", textvariable=date_entry_variable)
date_entry.grid(row=1, column=1, padx=10, pady=(20, 10))

def is_valid_date(date_str):
    try:
        datetime.strptime(date_str, "%d/%m/%Y")
        return True 
    except ValueError:
        return False  
    
def on_submit():
    entered_date = date_entry_variable.get()
    
    if not is_valid_date(entered_date):
        messagebox.showerror("Invalid Date", "Please enter a valid date in the format DD/MM/YYYY.")
    else:
        pass

#*********************************************************************
test_id_label = ctk.CTkLabel(frame_right_upload, text="Test ID:", font=("Arial", 18),
                            text_color=THEME_COLORS["main_text"])
test_id_label.grid(row=2, column=0, padx=20, pady=(10, 10), sticky="w")
test_id_variable = ctk.StringVar()
test_id_entry = ctk.CTkEntry(frame_right_upload, placeholder_text="000", textvariable=test_id_variable)
test_id_entry.grid(row=2, column=1, padx=10, pady=(10,10))

#===============================Subject==========================================
#*********************************************************************
subject_entry_variable = ctk.StringVar()
subject_label = ctk.CTkLabel(frame_right_upload, text="Subject:", font=("Arial", 18),
                            text_color=THEME_COLORS["main_text"])
subject_label.grid(row=3, column=0, padx=20, pady=(10, 10), sticky="w")
subject_entry_combobox = ctk.CTkComboBox(frame_right_upload, values=["PHYSICS", "MATHEMATICS", "CHEMISTRY"], 
                                        variable=subject_entry_variable, font=("Arial", 15), state="readonly")
subject_entry_combobox.grid(row=3, column=1, padx=10, pady=(10,10))

#=====================All three files upload=====================================
def open_file(file_label, file_path_var, filetypes):
    file_path = filedialog.askopenfilename(
        title="Select a File", 
        filetypes=filetypes 
    )
    
    if file_path:
        file_label.configure(text=file_path.split("/")[-1])
        file_path_var.set(file_path) 
        print(f"File Selected: {file_path}")
    else:
        print("No File Selected")

#=============================================================================================================
expanded_scorelist_file_label = ctk.CTkLabel(frame_right_upload, text="Expanded Scorelist File (.xlsx): ", 
                                            font=("Arial", 18), text_color=THEME_COLORS["main_text"])
expanded_scorelist_file_label.grid(row=4, column=0, padx=20, pady=(10,10), sticky="w")

expanded_scorelist_path = ctk.StringVar()

expanded_scorelist_file_button = ctk.CTkButton(frame_right_upload, text="Select File", font=("Arial", 18),
                                              fg_color=THEME_COLORS["button_bg"],
                                              text_color=THEME_COLORS["button_text"],
                                              hover_color=THEME_COLORS["hover_color"],
                                              command=lambda: open_file(expanded_scorelist_save_flile_label, expanded_scorelist_path, (("Excel Files", "*.xlsx;*.xls"),)))
expanded_scorelist_file_button.grid(row=4, column=1, padx=10, pady=(10,10))

expanded_scorelist_save_flile_label = ctk.CTkLabel(frame_right_upload, text="Expanded Scorelist Path",
                                                 text_color=THEME_COLORS["main_text"])
expanded_scorelist_save_flile_label.grid(row=4, column=2, padx=10, pady=(10,10), sticky="w")

#=============================================================================================================
student_analysis_file_label = ctk.CTkLabel(frame_right_upload, text="Student Analysis File (.xls): ", 
                                         font=("Arial", 18), text_color=THEME_COLORS["main_text"])
student_analysis_file_label.grid(row=5, column=0, padx=20, pady=(10,10), sticky="w")

student_analysis_path = ctk.StringVar()

student_analysis_file_button = ctk.CTkButton(frame_right_upload, text="Select File", font=("Arial", 18),
                                           fg_color=THEME_COLORS["button_bg"],
                                           text_color=THEME_COLORS["button_text"],
                                           hover_color=THEME_COLORS["hover_color"],
                                           command=lambda: open_file(student_analysis_save_flile_label, student_analysis_path, (("Excel Files", "*.xls"),)))
student_analysis_file_button.grid(row=5, column=1, padx=10, pady=(10,10))

student_analysis_save_flile_label = ctk.CTkLabel(frame_right_upload, text="Student Analysis Path",
                                               text_color=THEME_COLORS["main_text"])
student_analysis_save_flile_label.grid(row=5, column=2, padx=10, pady=(10,10), sticky="w")

#=============================================================================================================
blueprint_data_file_label = ctk.CTkLabel(frame_right_upload, text="Blueprint Data File (.pdf): ", 
                                       font=("Arial", 18), text_color=THEME_COLORS["main_text"])
blueprint_data_file_label.grid(row=6, column=0, padx=20, pady=(10,10), sticky="w")

blueprint_data_path = ctk.StringVar()

blueprint_data_file_button = ctk.CTkButton(frame_right_upload, text="Select File", font=("Arial", 18),
                                         fg_color=THEME_COLORS["button_bg"],
                                         text_color=THEME_COLORS["button_text"],
                                         hover_color=THEME_COLORS["hover_color"],
                                         command=lambda: open_file(blueprint_data_save_flile_label, blueprint_data_path, (("PDF Files", "*.pdf"),)))
blueprint_data_file_button.grid(row=6, column=1, padx=10, pady=(10,10))

blueprint_data_save_flile_label = ctk.CTkLabel(frame_right_upload, text="Blueprint Data Path",
                                             text_color=THEME_COLORS["main_text"])
blueprint_data_save_flile_label.grid(row=6, column=2, padx=10, pady=(10,10), sticky="w")

#=====================================Button that runs the code====================================================
#=========================================for the main thing=======================================================
def empty_variables():
    test_id_variable.set("")
    date_entry_variable.set("")
    subject_entry_variable.set("")
    expanded_scorelist_path.set("")
    student_analysis_path.set("")
    blueprint_data_path.set("")
    expanded_scorelist_save_flile_label.configure(text="Expanded Scorelist Path")
    student_analysis_save_flile_label.configure(text="Student Analysis Path")
    blueprint_data_save_flile_label.configure(text="Blueprint Data Path")

def create_log():
    now = datetime.now()
    date= now.date().strftime("%d/%m/%Y")
    path_save_to = r"Data/logs.csv"

    os.makedirs(os.path.dirname(path_save_to), exist_ok=True)
    file_exists = os.path.exists(path_save_to)

    with open(path_save_to, "a" if file_exists else "w", newline="") as file_log:
        columns = ["Test Details", "Test Date", "Upload Date"]
        file_obj = csv.DictWriter(file_log, fieldnames=columns)

        if not file_exists:
            file_obj.writeheader()

        file_obj.writerow({
            "Test Details": f"{date_entry_variable.get()}-{subject_entry_variable.get()}-{test_id_variable.get()}",
            "Test Date": date_entry_variable.get(),
            "Upload Date": date
        })

    print(f"{date_entry_variable.get()}-{subject_entry_variable.get()}-{test_id_variable.get()} saved on {date}")

# Add a progress bar
progress_bar = ctk.CTkProgressBar(frame_right_upload, orientation="horizontal", mode="determinate")
progress_bar.grid(row=8, column=0, columnspan=4, padx=20, pady=10, sticky="ew")
progress_bar.set(0)  # Initialize progress to 0

# Queue for communication between threads
task_queue = queue.Queue()

def run_main_code():
    """Handles validation and starts the processing thread."""
    if not expanded_scorelist_path.get() or not blueprint_data_path.get() or not student_analysis_path.get():
        messagebox.showerror("File not found", "Some file not uploaded or missing")
        return
    if not date_entry_variable.get():
        messagebox.showerror("Input Error", "Please enter a Date before proceeding.")
        return
    if not test_id_variable.get():
        messagebox.showerror("Input Error", "Please enter a Test ID before proceeding.")
        return
    if not subject_entry_variable.get():
        messagebox.showerror("Input Error", "Please enter a Subject before proceeding.")
        return

    # Disable the button to prevent multiple clicks
    run_analysis_button.configure(state="disabled")

    # Reset the progress bar
    progress_bar.set(0)

    # Start processing in a separate thread
    threading.Thread(target=process_data, daemon=True).start()

    # Start checking progress
    app.after(100, check_progress)

def process_data():
    """Runs the file validation and processing while updating progress."""
    try:
        # File validation
        if not file_check.main(student_analysis_path.get(), expanded_scorelist_path.get(), blueprint_data_path.get(),subject_entry_variable.get(),date_entry_variable.get(),test_id_variable.get()):
            task_queue.put(None)  # Stop progress
            messagebox.showerror("File Error", "Please recheck the files.")
            return
        
        # Check test ID and date validity
        if not file_check.check_if_date_exists(date_entry_variable.get(), test_id_variable.get(), subject_entry_variable.get()):
            task_queue.put(None)  # Stop progress
            messagebox.showerror("Invalid Test ID or Date", "Please check Test ID and Date")
            return

        # Simulate task progress
        for i in range(50):  # Halfway progress
            time.sleep(0.1)
            task_queue.put(i + 1)

        # Perform the actual processing
        upload_main.main(subject_entry_variable.get(), date_entry_variable.get(), test_id_variable.get(),
                         student_analysis_path.get(), expanded_scorelist_path.get(), blueprint_data_path.get())
        
        specific_data_main.main(expanded_scorelist_path.get(), date_entry_variable.get(), test_id_variable.get(), subject_entry_variable.get())

        # Complete progress
        for i in range(50, 100):  # Remaining progress
            time.sleep(0.1)
            task_queue.put(i + 1)

        # Task completed
        task_queue.put(None)

    except Exception as e:
        task_queue.put(None)  # Stop progress
        messagebox.showerror("Error", f"An error occurred: {str(e)}")

def check_progress():
    """Monitors the progress and updates the UI."""
    try:
        progress = task_queue.get_nowait()

        if progress is None:
            # Task completed
            run_analysis_button.configure(state="normal")
            progress_bar.set(1)  # Set to 100%
            messagebox.showinfo("Test Analysis Report", "Test Analysis Done!")
            create_log()
            refresh_frame(frame_right_history)
            empty_variables()
        else:
            # Update the progress bar
            progress_bar.set(progress / 100)
            app.after(100, check_progress)  # Continue checking progress
    except queue.Empty:
        # No updates yet, check again later
        app.after(100, check_progress)

run_analysis_button = ctk.CTkButton(frame_right_upload, text="Run Test Analysis", width=175, height=40,
                                   font=("Arial", 18), fg_color=THEME_COLORS["button_bg"],
                                   text_color=THEME_COLORS["button_text"],
                                   hover_color=THEME_COLORS["hover_color"],
                                   command=lambda: (on_submit(), run_main_code()))
run_analysis_button.grid(row=7, column=1, padx=15, pady=(10,10), sticky="w")

#===================================students======================================= 
#==================================================================================
# Create a main container frame to better organize the content
main_container = ctk.CTkFrame(frame_right_students, fg_color=THEME_COLORS["main_bg"])
main_container.grid(row=0, column=0, sticky="nsew", padx=10, pady=5)
frame_right_students.grid_columnconfigure(0, weight=1)

students_label = ctk.CTkLabel(main_container, text="Students", font=("Arial", 20, "bold"),
                            text_color=THEME_COLORS["main_text"])
students_label.grid(row=0, column=0, columnspan=4, sticky="w", padx=10, pady=(10,5))

#*********************************************************************
# First row - Student Type and Roll No
selection_frame = ctk.CTkFrame(main_container, fg_color=THEME_COLORS["main_bg"])
selection_frame.grid(row=1, column=0, columnspan=4, sticky="ew", padx=5, pady=5)

class_individual_variable = ctk.StringVar()
individual_rbutton = ctk.CTkRadioButton(selection_frame, text="Individual Student", font=("Arial", 14),
                                      variable=class_individual_variable, value="individual",
                                      text_color=THEME_COLORS["main_text"])
individual_rbutton.grid(row=0, column=0, padx=(5,10), pady=5)

class_rbutton = ctk.CTkRadioButton(selection_frame, text="Class", font=("Arial", 14),
                                  variable=class_individual_variable, value="class",
                                  text_color=THEME_COLORS["main_text"])
class_rbutton.grid(row=0, column=1, padx=10, pady=5)

roll_no_label = ctk.CTkLabel(selection_frame, text="Roll No:", font=("Arial", 14),
                           text_color=THEME_COLORS["main_text"])
roll_no_label.grid(row=0, column=2, padx=(20,5), pady=5)

roll_no_variable_students = ctk.StringVar()
roll_no_entry = ctk.CTkEntry(selection_frame, placeholder_text="20XXXXX", 
                            textvariable=roll_no_variable_students, state="disabled", width=120)
roll_no_entry.grid(row=0, column=3, padx=5, pady=5)

def toggle_roll_no_entry(*args):
    if class_individual_variable.get() == "individual":
        roll_no_entry.configure(state="normal")
    else:
        roll_no_entry.configure(state="disabled")

# Trace changes in the radio button variable
class_individual_variable.trace_add("write", toggle_roll_no_entry)

#========================================================================================
#*********************************************************************
# Second row - Subject Selection
subject_frame = ctk.CTkFrame(main_container, fg_color=THEME_COLORS["main_bg"])
subject_frame.grid(row=2, column=0, columnspan=4, sticky="ew", padx=5, pady=5)

subject_label_students = ctk.CTkLabel(subject_frame, text="Subject:", font=("Arial", 14),
                                    text_color=THEME_COLORS["main_text"])
subject_label_students.grid(row=0, column=0, padx=(5,5), pady=5, sticky="w")

subject_entry_variable_students = ctk.StringVar()
subject_entry_combobox_students = ctk.CTkComboBox(
    subject_frame, 
    values=["PHYSICS", "MATHEMATICS", "CHEMISTRY", "All (doesn't work)"],
    variable=subject_entry_variable_students, 
    font=("Arial", 14), 
    state="readonly",
    width=200
)
subject_entry_combobox_students.grid(row=0, column=1, padx=5, pady=5, sticky="w")

#==========================================================================================
#*********************************************************************
# Third row - Performance Type and Topic
performance_frame = ctk.CTkFrame(main_container, fg_color=THEME_COLORS["main_bg"])
performance_frame.grid(row=3, column=0, columnspan=4, sticky="ew", padx=5, pady=5)

overall_chapter_variable = ctk.StringVar()
overall_rbutton = ctk.CTkRadioButton(performance_frame, text="Overall Performance", font=("Arial", 14),
                                    variable=overall_chapter_variable, value="overall",
                                    text_color=THEME_COLORS["main_text"])
overall_rbutton.grid(row=0, column=0, padx=(5,10), pady=5)

chapterwise_rbutton = ctk.CTkRadioButton(performance_frame, text="Topicwise Performance", font=("Arial", 14),
                                        variable=overall_chapter_variable, value="chapterwise",
                                        text_color=THEME_COLORS["main_text"])
chapterwise_rbutton.grid(row=0, column=1, padx=10, pady=5)

chapter_students_label = ctk.CTkLabel(performance_frame, text="Topic:", font=("Arial", 14),
                                    text_color=THEME_COLORS["main_text"])
chapter_students_label.grid(row=0, column=2, padx=(20,5), pady=5)

chapter_variable_students = ctk.StringVar()
chapter_students_list = ctk.CTkComboBox(performance_frame, values=["hi"], 
                                      variable=chapter_variable_students, state="disabled",
                                      width=150)
chapter_students_list.grid(row=0, column=3, padx=5, pady=5)

def toggle_chapter_entry(*args):
    if overall_chapter_variable.get() == "chapterwise" and subject_entry_variable_students.get() != "All":
        chapter_students_list.configure(state="readonly")
    else:
        chapter_students_list.configure(state="disabled")

overall_chapter_variable.trace_add("write", toggle_chapter_entry)

#*********************************************************************
mathematics_chapters = ['Algebra', 'Trigonometry', 'Coordinate Geometry', 'Calculus', 
                    'Statistics and Probability', 'Linear Programming', 'Vector Algebra']
phyiscs_chapters = ['Mechanics', 'Thermodynamics and Kinetic Theory', 'Waves and Oscillations', 
                    'Electricity and Magnetism', 'Optics', 'Modern Physics']
chemistry_chapters = ['Physical Chemistry', 'Inorganic Chemistry', 'Organic Chemistry']

def display_list_subject_chapters(*args):
    if subject_entry_variable_students.get() == "All":
        chapterwise_rbutton.configure(state="disabled")
        chapter_students_list.configure(state="disabled")
        
        overall_chapter_variable.set("overall")
        chapter_students_list.set("")
        chapter_variable_students.set("")
        
    else:
        chapterwise_rbutton.configure(state="normal")
        chapter_students_list.configure(state="readonly")

        if subject_entry_variable_students.get() == "PHYSICS":
            chapter_students_list.configure(values=phyiscs_chapters)
        elif subject_entry_variable_students.get() == "MATHEMATICS":
            chapter_students_list.configure(values=mathematics_chapters)
        elif subject_entry_variable_students.get() == "CHEMISTRY":
            chapter_students_list.configure(values=chemistry_chapters)
        
        chapter_students_list.set("")
        chapter_variable_students.set("")
        toggle_chapter_entry()

subject_entry_variable_students.trace_add("write", display_list_subject_chapters)

#*********************************************************************
chapter_index_students = ""  # Reset index on any change
def get_chapter_index(*args):
    global chapter_index_students
    
    if overall_chapter_variable.get() == "chapterwise" and subject_entry_variable_students.get() != "All":
        try:
            if subject_entry_variable_students.get() == "Physics":
                chapter_index_students = phyiscs_chapters.index(chapter_variable_students.get())
            elif subject_entry_variable_students.get() == "Mathematics":
                chapter_index_students = mathematics_chapters.index(chapter_variable_students.get())
            elif subject_entry_variable_students.get() == "Chemistry":
                chapter_index_students = chemistry_chapters.index(chapter_variable_students.get())
            print(f"Chapter Index Updated: {chapter_index_students}")
        except ValueError as e:
            print(f"Error: Chapter or Subject not found. {e}")

overall_chapter_variable.trace_add("write", get_chapter_index)
chapter_variable_students.trace_add("write", get_chapter_index)

#*********************************************************************
def check_missing_fields_students():
    if class_individual_variable.get() == "individual" and not roll_no_variable_students.get():
        messagebox.showerror("Missing Input", "Please enter the roll number before proceeding.")
    if not subject_entry_variable_students.get():
        messagebox.showerror("Missing Input", "Please enter the subject before proceeding.")
    if not chapter_variable_students.get() and overall_chapter_variable.get() == "chapterwise":
        messagebox.showerror("Missing Input", "Please enter the topic before proceeding.")

def clear_fields_students():
    class_individual_variable.set("")
    roll_no_variable_students.set("")
    subject_entry_variable_students.set("")
    overall_chapter_variable.set("")
    chapter_variable_students.set("")


#*********************************************************************

def retrieve_data(roll, student_data_path):
    # Read student names from CSV
    student_records = pd.read_csv("Data/student_names.csv") 
    student_numbers=list(student_records["Roll Number"])
    student=list(student_records["Name"])[student_numbers.index(int(roll))]
    total_students=len(student_numbers)
    with open(student_data_path, "r") as file:
        student_data = json.load(file)
    
    # Extract the latest test record
    try:
        latest_test = student_data[-1]  # Assuming the last entry is the latest
    except KeyError:
        latest_test=student_data
    finally:
        latest_test_key = list(latest_test.keys())[0]  # Get the test key (e.g., "05/01/2025-PHYSICS-101")
        rank = latest_test[latest_test_key]["Rank"]  # Extract the rank
        
    return student, rank, total_students
#*********************************************************************
def generate_graph(roll_no, subject,state=False):
    check_missing_fields_students()
    student_data_path = f"Data/Processed/{subject}/{roll_no}.json"
    common_data_path = f"Data/Processed/{subject}/common_data.json"
    shared_state.update_values(new_name=retrieve_data(roll_no,student_data_path)[0],new_rollno=roll_no,new_rank=retrieve_data(roll_no,student_data_path)[1],new_subject=subject_entry_variable_students.get(),new_total_students=retrieve_data(roll_no,student_data_path)[2])
    if not state:
        webbrowser.open("http://127.0.0.1:8000") 
    else:
        pass
    clear_fields_students()


def download_pdf():
    url = "http://127.0.0.1:8000/d"
    response = requests.get(url, stream=True)  

get_data_button = ctk.CTkButton(main_container, text="Generate Data", 
                               width=150, height=35, font=("Arial", 14),
                               fg_color=THEME_COLORS["button_bg"],
                               text_color=THEME_COLORS["button_text"],
                               hover_color=THEME_COLORS["hover_color"],
                               command=lambda: generate_graph(roll_no_variable_students.get(),subject_entry_variable_students.get()))
download_coloured_button = ctk.CTkButton(main_container, text="Download Coloured", 
                               width=150, height=35, font=("Arial", 14),
                               fg_color=THEME_COLORS["button_bg"],
                               text_color=THEME_COLORS["button_text"],
                               hover_color=THEME_COLORS["hover_color"],
                               command=lambda: (generate_graph(roll_no_variable_students.get(),subject_entry_variable_students.get(),state=True),download_pdf()))
get_data_button.grid(row=4, column=0, columnspan=4, pady=10)
download_coloured_button.grid(row=4, column=0,columnspan=3,pady=10)

#===================================Download======================================= 
#==================================================================================
# Setup Settings Page
download_label = ctk.CTkLabel(frame_right_download, text="Download", font=("Arial", 24, "bold"),
                             text_color=THEME_COLORS["main_text"])
download_label.grid(row=0, column=0, padx=20, pady=20)

download_students_class_var = ctk.StringVar()
students_report_rbutton = ctk.CTkRadioButton(frame_right_download, text="Students' Report", font=("Arial", 18),
                                      variable=download_students_class_var, value="students",
                                      text_color=THEME_COLORS["main_text"])
students_report_rbutton.grid(row=1, column=0, padx=(25,10), pady=5)

class_rbutton = ctk.CTkRadioButton(frame_right_download, text="Class", font=("Arial", 18),
                                  variable=download_students_class_var, value="class",
                                  text_color=THEME_COLORS["main_text"])
class_rbutton.grid(row=1, column=1, padx=10, pady=5)

#===================================History======================================== 
#==================================================================================
def load_logs():
    log_file = "Data/logs.csv"
    if not os.path.exists(log_file):
        return []  

    with open(log_file, "r", newline="") as file:
        reader = csv.reader(file)
        data = list(reader) 

    for test in data[1:]:
        date_test, subj, id = test[0].split("-")
        if subj == "PHYSICS":
            test[0] = f"PH{id}"
        elif subj == "MATHEMATICS":
            test[0] = f"MA{id}"
        elif subj == "CHEMISTRY":
            test[0] = f"CY{id}"
    return data

def delete_entries():
    id_thing = ""
    subj, to_delete_id = delete_entry_var.get()[:2], delete_entry_var.get()[-3:]
    if subj == "PH":
        id_thing = f"PHYSICS-{to_delete_id}"
        subj = "PHYSICS"
    elif subj == "CY":
        id_thing = f"CHEMISTRY-{to_delete_id}"
        subj = "CHEMISTRY"
    elif subj == "MA":
        id_thing = f"MATHEMATICS-{to_delete_id}"
        subj = "MATHEMATICS"
    else:
        messagebox.showerror("Invalid ID", "Please enter the correct Test ID.")
        return
    
    logs_path = r"Data/logs.csv"
    with open(logs_path, "r") as logs_file_check:
        log_reader = csv.reader(logs_file_check)
        found_entry = False
        for row in log_reader:
            if row[0].endswith(id_thing) and row:
                found_entry = True
                break
    if not found_entry:
        messagebox.showerror("Invalid ID", "The given Test ID doesn't exist")
        return
                

    try:
        roll_file_path = r"Data/student_names.csv"
        roll_numbers = []

        with open(roll_file_path, "r", newline="") as csvfile:
            reader = csv.reader(csvfile)
            next(reader, None)
            for row in reader:
                if len(row) >= 1:
                    roll_numbers.append(row[0].strip())
        
        # REMOVING UNPROCESSED DATA
        for roll_no in roll_numbers:
            roll_no_path = rf"Data/{subj}/{roll_no}.csv"
            filtered_rows = []

            with open(roll_no_path, "r", newline="") as csvfile:
                reader = csv.reader(csvfile)
                header = next(reader)

                for row in reader:
                    if len(row) >= 3 and row[2] != to_delete_id:
                        filtered_rows.append(row)

            with open(roll_no_path, "w", newline="") as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow(header)

                for row in filtered_rows:
                    writer.writerow(row)
        
        # REMOVING PROCESSED DATA (Individual Student Files)
        for roll_no in roll_numbers:
            roll_no_processed_path = f"Data/Processed/{subj}/{roll_no}.json"

            if not os.path.exists(roll_no_processed_path):
                continue  # Skip if the file doesn't exist

            with open(roll_no_processed_path, "r") as file:
                data = json.load(file)  # Data is a LIST of dictionaries

            # Remove only the dictionary containing the specific test entry
            if isinstance(data, dict):
                key = next(iter(data))
                if key.endswith(id_thing):
                    os.remove(roll_no_processed_path)  # Delete entire file if single dictionary matches

            elif isinstance(data, list):
                filtered_data = []
                for dict_data in data:
                    key_dict = next(iter(dict_data))  # Extract key from each dictionary
                    if not key_dict.endswith(id_thing):  # Keep only unmatched entries
                        filtered_data.append(dict_data)

                # If no data remains, delete the file; otherwise, save updated data
                if filtered_data:
                    with open(roll_no_processed_path, "w") as file:
                        json.dump(filtered_data, file, indent=4)
                else:
                    os.remove(roll_no_processed_path)  # Delete file when empty

        # REMOVING PROCESSED DATA (Common File)
        common_processed_path = f"Data/Processed/{subj}/common_data.json"

        if os.path.exists(common_processed_path):
            with open(common_processed_path, "r") as file:
                data = json.load(file)  # Data is a LIST of dictionaries

            # Remove only the specific test entry
            if isinstance(data, dict):
                key = next(iter(data))
                if key.endswith(id_thing):
                    os.remove(common_processed_path)  # Delete entire file if single dictionary matches

            elif isinstance(data, list):
                filtered_data = []
                for dict_data in data:
                    key_dict = next(iter(dict_data))  # Extract key from each dictionary
                    if not key_dict.endswith(id_thing):  # Keep only unmatched entries
                        filtered_data.append(dict_data)

                # If no data remains, delete the file; otherwise, save updated data
                if filtered_data:
                    with open(common_processed_path, "w") as file:
                        json.dump(filtered_data, file, indent=4)
                else:
                    os.remove(common_processed_path)  # Delete file when empty

        # Deleting last log!
        with open(logs_path, "r", newline="") as file:
            reader = csv.reader(file)
            headers = next(reader) 
            logs = [row for row in reader if not row[0].endswith(id_thing)]

        with open(logs_path, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(headers) 
            writer.writerows(logs)
    except FileNotFoundError:
        pass
    messagebox.showinfo("Success", f"Test {to_delete_id} has been deleted successfully!")
    refresh_frame(frame_right_history)

delete_entry_var = ctk.StringVar()
def refresh_frame(frame):
    delete_entry_var.set("")
    
    for widget in frame.winfo_children():
        widget.destroy()
    
    logs = load_logs()

    frame.configure(bg_color=THEME_COLORS["main_bg"])

    scrollable_frame = ctk.CTkScrollableFrame(frame_right_history, width=650, height=400,
                                             bg_color=THEME_COLORS["main_bg"],
                                             fg_color=THEME_COLORS["main_bg"],
                                             scrollbar_fg_color="#050535",
                                             scrollbar_button_color="#d3d3d3",  
                                             scrollbar_button_hover_color="#a9a9a9"
                                            )
    scrollable_frame.pack(expand=True, fill="both")

    delete_frame = ctk.CTkFrame(scrollable_frame, bg_color=THEME_COLORS["main_bg"],
                               fg_color=THEME_COLORS["main_bg"])
    delete_frame.pack(pady=2, side="top")

    delete_label = ctk.CTkLabel(delete_frame, text="Enter ID: ", font=("Arial", 14),
                                bg_color=THEME_COLORS["main_bg"])
    delete_label.grid(row=0, column=0, padx=5, pady=5)

    delete_entry = ctk.CTkEntry(delete_frame, placeholder_text="SU000", textvariable=delete_entry_var,
                                fg_color="white", bg_color=THEME_COLORS["main_bg"])
    delete_entry.grid(row=0, column=1, padx=5, pady=5)

    delete_butoon = ctk.CTkButton(delete_frame, text="Delete", command=delete_entries,
                                   fg_color=THEME_COLORS["button_bg"], hover_color=THEME_COLORS["hover_color"],
                                   bg_color=THEME_COLORS["main_bg"]
                                   )    
    delete_butoon.grid(row=0, column=2, padx=5, pady=5)

    table = CTkTable(
        master=scrollable_frame,
        row=len(logs), 
        column=3,
        values=[logs[0]] + sorted(logs[1:], reverse=True),
        corner_radius=3,
        bg_color=THEME_COLORS["main_bg"],
        fg_color=THEME_COLORS["main_bg"],
    )
    table.pack(expand=True, fill="both", padx=20, pady=20)

try:
    refresh_frame(frame_right_history)
except IndexError:
    pass

app.resizable(False, False)
app.mainloop()
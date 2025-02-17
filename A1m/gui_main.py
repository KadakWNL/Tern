import customtkinter as ctk
from tkinter import filedialog, messagebox
import upload_main
import specific_data_main
import file_check
import datetime

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

app = ctk.CTk()
app.geometry("854x480")
app.title("Tern - Student Progress Tracker")

# Grid Configuration for Layout
app.grid_columnconfigure(1, weight=1)  # Right frame expands
app.grid_rowconfigure(0, weight=1)

# Left Frame (Navbar)
frame_left = ctk.CTkFrame(app, width=200, border_width=0, fg_color="#2C2F33")
frame_left.grid(row=0, column=0, sticky="ns")

# Main Content Area (Right Frame)
frame_container = ctk.CTkFrame(app, border_width=0)
frame_container.grid(row=0, column=1, padx=20, pady=20, sticky="nsew")

# Different Right Frames for Each Page
frame_right_upload = ctk.CTkFrame(frame_container, border_width=0)
frame_right_students = ctk.CTkFrame(frame_container, border_width=0)
frame_right_download = ctk.CTkFrame(frame_container, border_width=0)

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
head_label = ctk.CTkLabel(frame_left, text="Tern", font=("Arial", 30, "bold"))
head_label.pack(pady=(30, 10))

sub_label = ctk.CTkLabel(frame_left, text="Progress Tracker", font=("Arial", 14))
sub_label.pack(pady=(0, 30))

nav_button1 = ctk.CTkButton(frame_left, text="Download", fg_color="transparent", hover_color="#4E5257", 
                            command=lambda: show_frame(frame_right_download))
nav_button1.pack(fill="x", pady=5)

nav_button2 = ctk.CTkButton(frame_left, text="Students", fg_color="transparent", hover_color="#4E5257",
                            command=lambda: show_frame(frame_right_students))
nav_button2.pack(fill="x", pady=5)

nav_button3 = ctk.CTkButton(frame_left, text="Upload", fg_color="transparent", hover_color="#4E5257",
                            command=lambda: show_frame(frame_right_upload))
nav_button3.pack(fill="x", pady=5)


#==============================Test Analysis======================================= 
#==================================================================================
frame_test_analysis_label = ctk.CTkLabel(frame_right_upload, text="Test Analysis", font=("Arial", 24, "bold"))
frame_test_analysis_label.grid(row=0, column=0, columnspan=4, sticky="ew", pady=10)

#=====================Data and Test Id Entry===================================
#*********************************************************************
date_label = ctk.CTkLabel(frame_right_upload, text="Date(DD/MM/YYYY):", font=("Arial", 18))
date_label.grid(row=1, column=0, padx=20, pady=(20, 10), sticky="w")
date_entry_variable = ctk.StringVar()
date_entry = ctk.CTkEntry(frame_right_upload, placeholder_text="DD/MM/YYYY", textvariable=date_entry_variable)
date_entry.grid(row=1, column=1, padx=10, pady=(20, 10))

def is_valid_date(date_str):
    try:
        datetime.datetime.strptime(date_str, "%d/%m/%Y")
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
test_id_label = ctk.CTkLabel(frame_right_upload, text="Test ID:", font=("Arial", 18))
test_id_label.grid(row=2, column=0, padx=20, pady=(10, 10), sticky="w")
test_id_variable = ctk.StringVar()
test_id_entry = ctk.CTkEntry(frame_right_upload, placeholder_text="000", textvariable=test_id_variable)
test_id_entry.grid(row=2, column=1, padx=10, pady=(10,10))

#===============================Subject==========================================
#*********************************************************************
subject_entry_variable = ctk.StringVar()
subject_label = ctk.CTkLabel(frame_right_upload, text="Subject:", font=("Arial", 18))
subject_label.grid(row=3, column=0, padx=20, pady=(10, 10), sticky="w")
subject_entry_combobox = ctk.CTkComboBox(frame_right_upload, values=["PHYSICS", "MATHEMATICS", "CHEMISTRY"], variable=subject_entry_variable, font=("Arial", 15), state="readonly")
subject_entry_combobox.grid(row=3, column=1, padx=10, pady=(10,10))

#=====================All three files upload=====================================
def open_file(file_label, file_path_var, filetypes):
    file_path = filedialog.askopenfilename(
        title="Select a File", 
        filetypes=filetypes 
    )
    
    if file_path:
        # print("File Successfully uploaded")
        file_label.configure(text=file_path.split("/")[-1])
        file_path_var.set(file_path) 
        print(file_path)
        print("No file selected")

#=============================================================================================================
expanded_scorelist_file_label = ctk.CTkLabel(frame_right_upload, text="Expanded Scorelist File (.xlsx): ", font=("Arial", 18))
expanded_scorelist_file_label.grid(row=4, column=0, padx=20, pady=(10,10), sticky="w")

expanded_scorelist_path = ctk.StringVar()

expanded_scorelist_file_button = ctk.CTkButton(frame_right_upload, text="Select File", font=("Arial", 18),
                                                command=lambda: open_file(expanded_scorelist_save_flile_label, expanded_scorelist_path, (("Excel Files", "*.xlsx;*.xls"),)))
expanded_scorelist_file_button.grid(row=4, column=1, padx=10, pady=(10,10))

expanded_scorelist_save_flile_label = ctk.CTkLabel(frame_right_upload, text="Expanded Scorelist Path")
expanded_scorelist_save_flile_label.grid(row=4, column=2, padx=10, pady=(10,10), sticky="w")

#=============================================================================================================
student_analysis_file_label = ctk.CTkLabel(frame_right_upload, text="Student Analysis File (.xls): ", font=("Arial", 18))
student_analysis_file_label.grid(row=5, column=0, padx=20, pady=(10,10), sticky="w")

student_analysis_path = ctk.StringVar()

student_analysis_file_button = ctk.CTkButton(frame_right_upload, text="Select File", font=("Arial", 18),
                                            command=lambda: open_file(student_analysis_save_flile_label, student_analysis_path, (("Excel Files", "*.xls"),)))
student_analysis_file_button.grid(row=5, column=1, padx=10, pady=(10,10))

student_analysis_save_flile_label = ctk.CTkLabel(frame_right_upload, text="Student Analysis Path")
student_analysis_save_flile_label.grid(row=5, column=2, padx=10, pady=(10,10), sticky="w")

#=============================================================================================================
blueprint_data_file_label = ctk.CTkLabel(frame_right_upload, text="Blueprint Data File (.pdf): ", font=("Arial", 18))
blueprint_data_file_label.grid(row=6, column=0, padx=20, pady=(10,10), sticky="w")

blueprint_data_path = ctk.StringVar()

blueprint_data_file_button = ctk.CTkButton(frame_right_upload, text="Select File", font=("Arial", 18),
                                            command=lambda: open_file(blueprint_data_save_flile_label, blueprint_data_path, (("PDF Files", "*.pdf"),)))
blueprint_data_file_button.grid(row=6, column=1, padx=10, pady=(10,10))

blueprint_data_save_flile_label = ctk.CTkLabel(frame_right_upload, text="Blueprint Data Path")
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

def run_main_code():
    # print(expanded_scorelist_path.get(), student_analysis_path.get(), blueprint_data_path.get())
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
    if file_check.main(student_analysis_path.get(),expanded_scorelist_path.get(),blueprint_data_path.get(),subject_entry_variable.get()):
        upload_main.main(subject_entry_variable.get(),date_entry_variable.get(),test_id_variable.get(),
                        student_analysis_path.get(),expanded_scorelist_path.get(),blueprint_data_path.get())
        specific_data_main.main(date_entry_variable.get(), test_id_variable.get(), subject_entry_variable.get())
        messagebox.showinfo("Test Analysis Report", "Test Analysis Done!")
    else:
        messagebox.showerror("File Error","Please recheck the files.")

    empty_variables()
    
run_analysis_button = ctk.CTkButton(frame_right_upload, text="Run Test Analysis", width=175, height=40,font=("Arial", 18), command=lambda: (on_submit(), run_main_code()))
run_analysis_button.grid(row=7, column=1, padx=15, pady=(10,10), sticky="w")

#===================================students======================================= 
#==================================================================================
students_label = ctk.CTkLabel(frame_right_students, text="Students", font=("Arial", 24, "bold"))
students_label.grid(row=0, column=0, sticky="ew",padx=20, pady=20)

class_individual_variable = ctk.StringVar()

individual_rbutton = ctk.CTkRadioButton(frame_right_students, text="Individual Student", font=("Arial", 18),
                                            variable=class_individual_variable, value="individual")
individual_rbutton.grid(row=1, column=0, padx=10, pady=(10,10), sticky="w")
class_rbutton = ctk.CTkRadioButton(frame_right_students, text="Class", font=("Arial", 18),
                                            variable=class_individual_variable, value="class")
class_rbutton.grid(row=1, column=1, padx=10, pady=(10,10), sticky="w")

#*********************************************************************
roll_no_variable = ctk.StringVar()
roll_no_label = ctk.CTkLabel(frame_right_students, text="Roll No:", font=("Arial", 18))
roll_no_label.grid(row=1, column=2, padx=10, pady=(10,10), sticky="w")
roll_no_entry = ctk.CTkEntry(frame_right_students, placeholder_text="20XXXXX", textvariable=roll_no_variable, state="disabled")
roll_no_entry.grid(row=1, column=3, padx=10, pady=(10,10), sticky="w")

def toggle_roll_no_entry(*args):
    if class_individual_variable.get() == "individual":
        roll_no_entry.configure(state="normal")
    else:
        roll_no_entry.configure(state="disabled")

# Trace changes in the radio button variable
class_individual_variable.trace_add("write", toggle_roll_no_entry)

#========================================================================================
#*********************************************************************
subject_entry_variable_students = ctk.StringVar()
subject_label_students = ctk.CTkLabel(frame_right_students, text="Subject:", font=("Arial", 18))
subject_label_students.grid(row=2, column=0, padx=10, pady=(10, 10), sticky="w")
subject_entry_combobox_students = ctk.CTkComboBox(frame_right_students, values=["Physics", "Mathematics", "Chemistry", "All"],
                                                    variable=subject_entry_variable_students, font=("Arial", 15), state="readonly")
subject_entry_combobox_students.grid(row=2, column=1, padx=10, pady=(10,10))

#==========================================================================================

overall_chapter_variable = ctk.StringVar()

overall_rbutton = ctk.CTkRadioButton(frame_right_students, text="Overall Performance", font=("Arial", 18),
                                        variable=overall_chapter_variable, value="overall")
overall_rbutton.grid(row=4, column=0, padx=10, pady=(10,10), sticky="w")

chapterwise_rbutton = ctk.CTkRadioButton(frame_right_students, text="Chapterwise Performance", font=("Arial", 18),
                                            variable=overall_chapter_variable, value="chapterwise")
chapterwise_rbutton.grid(row=4, column=1, padx=10, pady=(10,10), sticky="w")

#*********************************************************************
chapter_variable_students = ctk.StringVar()
chapter_students_label = ctk.CTkLabel(frame_right_students, text="Chapter:", font=("Arial", 18))
chapter_students_label.grid(row=4, column=2, padx=10, pady=(10,10), sticky="w")

chapter_students_list = ctk.CTkComboBox(frame_right_students, values=["hi"], 
                                        variable=chapter_variable_students, state="disabled")
chapter_students_list.grid(row=4, column=3, padx=10, pady=(10,10), sticky="w")

def toggle_chapter_entry(*args):
    if overall_chapter_variable.get() == "chapterwise" and subject_entry_variable_students.get() != "All":
        chapter_students_list.configure(state="readonly")
    else:
        chapter_students_list.configure(state="disabled")

overall_chapter_variable.trace_add("write", toggle_chapter_entry)

#*********************************************************************
mathematics_chapters = ["math chapters"]
phyiscs_chapters = ["phy chapters"]
chemistry_chapters = ["chem chapters"]

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

        if subject_entry_variable_students.get() == "Physics":
            chapter_students_list.configure(values=phyiscs_chapters)
        elif subject_entry_variable_students.get() == "Mathematics":
            chapter_students_list.configure(values=mathematics_chapters)
        else:
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


overall_chapter_variable.trace_add("write",get_chapter_index)
chapter_variable_students.trace_add("write",get_chapter_index)
print(chapter_index_students)






#===================================Download======================================= 
#==================================================================================


# Setup Settings Page
download_label = ctk.CTkLabel(frame_right_download, text="Download", font=("Arial", 24, "bold"))
download_label.grid(row=0, column=0, padx=20, pady=20)

app.mainloop()

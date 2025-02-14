import customtkinter as ctk
from tkinter import filedialog, messagebox

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

# Right Frame (Main Content)
frame_right = ctk.CTkFrame(app, border_width=0)
frame_right.grid(row=0, column=1, padx=20, pady=20, sticky="nsew")

# Navbar Widgets
head_label = ctk.CTkLabel(frame_left, text="Tern", font=("Arial", 30, "bold"))
head_label.pack(pady=(30, 10))

sub_label = ctk.CTkLabel(frame_left, text="Progress Tracker", font=("Arial", 14))
sub_label.pack(pady=(0, 30))

nav_button1 = ctk.CTkButton(frame_left, text="Dashboard", fg_color="transparent", hover_color="#4E5257")
nav_button1.pack(fill="x", pady=5)

nav_button2 = ctk.CTkButton(frame_left, text="Students", fg_color="transparent", hover_color="#4E5257")
nav_button2.pack(fill="x", pady=5)

nav_button3 = ctk.CTkButton(frame_left, text="Settings", fg_color="transparent", hover_color="#4E5257")
nav_button3.pack(fill="x", pady=5)

# Main Content Widgets
#==============================================================================
frame_test_analysis_label = ctk.CTkLabel(frame_right, text="Test Analysis", font=("Arial", 24, "bold"))
frame_test_analysis_label.grid(row=0, column=0, columnspan=4, sticky="ew", pady=10)

#=====================Data and Test Id Entry===================================
date_label = ctk.CTkLabel(frame_right, text="Date:", font=("Arial", 18))
date_label.grid(row=1, column=0, padx=20, pady=(20, 10), sticky="w")
date_entry_variable = ctk.StringVar()
date_entry = ctk.CTkEntry(frame_right, placeholder_text="DD/MM/YYYY", textvariable=date_entry_variable)
date_entry.grid(row=1, column=1, padx=10, pady=(20, 10))

test_id_label = ctk.CTkLabel(frame_right, text="Test ID:", font=("Arial", 18))
test_id_label.grid(row=2, column=0, padx=20, pady=(10, 10), sticky="w")
test_id_variable = ctk.StringVar()
test_id_entry = ctk.CTkEntry(frame_right, placeholder_text="000", textvariable=test_id_variable)
test_id_entry.grid(row=2, column=1, padx=10, pady=(10,10))

#=====================All three files upload=====================================
def open_file(file_label, file_path_var, filetypes):
    file_path = filedialog.askopenfilename(
        title="Select a File", 
        filetypes=filetypes  # Use the passed file types
    )
    
    if file_path:
        print("File Successfully uploaded")
        file_label.configure(text=file_path)  # Update the label with file path
        file_path_var.set(file_path)  # Store the file path in the variable
    else:
        print("No file selected")

#=============================================================================================================
expanded_scorelist_file_label = ctk.CTkLabel(frame_right, text="Expanded Scorelist File (.xlsx): ", font=("Arial", 18))
expanded_scorelist_file_label.grid(row=3, column=0, padx=20, pady=(10,10), sticky="w")

expanded_scorelist_path = ctk.StringVar()

expanded_scorelist_file_button = ctk.CTkButton(frame_right, text="Select File", font=("Arial", 18),
                                                command=lambda: open_file(expanded_scorelist_save_flile_label, expanded_scorelist_path, (("Excel Files", "*.xlsx;*.xls"),)))
expanded_scorelist_file_button.grid(row=3, column=1, padx=10, pady=(10,10))

expanded_scorelist_save_flile_label = ctk.CTkLabel(frame_right, text="Expanded Scorelist Path")
expanded_scorelist_save_flile_label.grid(row=3, column=2, padx=10, pady=(10,10), sticky="w")

#=============================================================================================================
student_analysis_file_label = ctk.CTkLabel(frame_right, text="Student Analysis File (.xls): ", font=("Arial", 18))
student_analysis_file_label.grid(row=4, column=0, padx=20, pady=(10,10), sticky="w")

student_analysis_path = ctk.StringVar()

student_analysis_file_button = ctk.CTkButton(frame_right, text="Select File", font=("Arial", 18),
                                              command=lambda: open_file(student_analysis_save_flile_label, student_analysis_path, (("Excel Files", "*.xls"),)))
student_analysis_file_button.grid(row=4, column=1, padx=10, pady=(10,10))

student_analysis_save_flile_label = ctk.CTkLabel(frame_right, text="Student Analysis Path")
student_analysis_save_flile_label.grid(row=4, column=2, padx=10, pady=(10,10), sticky="w")

#=============================================================================================================
blueprint_data_file_label = ctk.CTkLabel(frame_right, text="Blueprint Data File (.pdf): ", font=("Arial", 18))
blueprint_data_file_label.grid(row=5, column=0, padx=20, pady=(10,10), sticky="w")

blueprint_data_path = ctk.StringVar()

blueprint_data_file_button = ctk.CTkButton(frame_right, text="Select File", font=("Arial", 18),
                                            command=lambda: open_file(blueprint_data_save_flile_label, blueprint_data_path, (("PDF Files", "*.pdf"),)))
blueprint_data_file_button.grid(row=5, column=1, padx=10, pady=(10,10))

blueprint_data_save_flile_label = ctk.CTkLabel(frame_right, text="Blueprint Data Path")
blueprint_data_save_flile_label.grid(row=5, column=2, padx=10, pady=(10,10), sticky="w")


#=====================================Button that runs the code====================================================
#=========================================for the main thing=======================================================
def run_main_code():
    # print(expanded_scorelist_path.get(), student_analysis_path.get(), blueprint_data_path.get())
    if not expanded_scorelist_path.get() or not blueprint_data_path.get() or not student_analysis_path.get():
        messagebox.showerror("File not found", "Some file not uploaded or missing")
        return
    messagebox.showinfo("Test Analysis Report", "Test Analysis Done!")

run_analysis_button = ctk.CTkButton(frame_right, text="Run Test Analysis", width=175, height=40,font=("Arial", 18), command=run_main_code)
run_analysis_button.grid(row=6, column=1, padx=15, pady=(10,10), sticky="w")

app.mainloop()

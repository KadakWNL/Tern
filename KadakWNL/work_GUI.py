import customtkinter as ctk
from tkinter import filedialog

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")

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
#=====================Data and Test Id Entry===================================
date_label = ctk.CTkLabel(frame_right, text="Date:", font=("Arial", 18))
date_label.grid(row=0, column=0, padx=20, pady=(20, 10), sticky="w")
date_entry_variable = ctk.StringVar()
date_entry = ctk.CTkEntry(frame_right, placeholder_text="DD/MM/YYYY", textvariable=date_entry_variable)
date_entry.grid(row=0, column=1, padx=10, pady=(20, 10))

test_id_label = ctk.CTkLabel(frame_right, text="Test ID:", font=("Arial", 18))
test_id_label.grid(row=1, column=0, padx=20, pady=(10, 10), sticky="w")
test_id_variable = ctk.StringVar()
test_id_entry = ctk.CTkEntry(frame_right, placeholder_text="000", textvariable=test_id_variable)
test_id_entry.grid(row=1, column=1, padx=10, pady=(10,10))

#=====================All three files upload=====================================
def open_file():
    file_path = filedialog.askopenfilename(title="Select an Excel File", filetypes=(("Excel Files", "*.xlsx;*.xls"), ("All Files", "*.*")))
    if file_path:
        print("File Successfully uploaded")
    else:
        print("File not found!")

expanded_scorelist_file_label = ctk.CTkLabel(frame_right, text="Expanded Scorelist File (.xlsx): ", font=("Arial", 18))
expanded_scorelist_file_label.grid(row=3, column=0, padx=10, pady=(10,10))
expanded_scorelist_file_button = ctk.CTkButton(frame_right, text="Select File", font=("Arial", 18), command=open_file)
expanded_scorelist_file_button.grid(row=3, column=1, padx=10, pady=(10,10))

app.mainloop()

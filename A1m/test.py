import customtkinter as ctk

ctk.set_appearance_mode("light")  # Try "dark" if you feel fancy!

root = ctk.CTk()
root.geometry("400x200")

entry = ctk.CTkEntry(root, placeholder_text="Type something...")
entry.pack(padx=20, pady=20)

root.mainloop()
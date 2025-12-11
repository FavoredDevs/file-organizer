import tkinter as tk
from tkinter import filedialog
import os, shutil

window = tk.Tk()
window.title("📁 File Organizer")
window.geometry("400x250")
window.configure(bg="#000")

# Status variable
status_var = tk.StringVar(
                    value="Ready to Organize")
tk.Label(window, textvariable=status_var,
         bg="#111", fg="#0ff",
         font=("Calibri", 16, "bold"),
         height=2).pack(fill="x",
                        padx=10, pady=20)

TYPES = {
    "Images": [".jpg", ".png", ".jpeg", ".gif", ".HEIC"],
    "Docs": [".pdf", ".docx", ".txt", ".pages", ".xlsx", ".csv"],
    "Videos": [".mp4", ".mov", ".avi"],
    "Audio": [".mp3", ".wav"],
    "Code": [".py", ".md"]
}

def organize_file(event): # 'event' argument is necessary for binding
    folder = filedialog.askdirectory()
    if not folder: return

    count = 0
    for file in os.listdir(folder):
        # Skip directories and files without an extension
        if os.path.isdir(os.path.join(folder, file)) or "." not in file: continue
        
        ext = os.path.splitext(file)[1].lower()

        for category, extensions in TYPES.items():
            if ext in extensions:
                target_dir = os.path.join(
                    folder, category)
                if not os.path.exists(
                    target_dir): os.makedirs(target_dir)
                
                # Use shutil.move to move the file
                shutil.move(os.path.join(
                    folder, file), os.path.join(
                        target_dir, file
                    ))
                count += 1
                break
                
    status_var.set(f"Moved {count} Files! ✨")

frame = tk.Frame(window, bg="blue")
frame.pack(pady=20)

btn_text = "SELECT FOLDER"
btn_widget = tk.Label(
    frame, # Pack into frame
    text=btn_text, # Added text
    font=("Calibri", 14, "bold"),
    bg="#f39c12", fg="white",
    width=20, height=2,
    relief="flat")
    
btn_widget.bind("<Button-1>", organize_file) 

btn_widget.pack()

tk.Label(window, text="Sorts: Images, Docs, ...",
         bg="#000", fg="#555",
         font=("Calibri", 10)).pack(
             side="bottom", pady=10)

window.mainloop()
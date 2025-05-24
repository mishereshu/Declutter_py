import os
import shutil
from pathlib import Path
from tkinter import Tk, Button, Label, messagebox
import platform

# Detect Downloads folder
if platform.system() == "Windows":
    DOWNLOADS = Path(os.environ["USERPROFILE"]) / "Downloads"
else:
    DOWNLOADS = Path.home() / "Downloads"

# File categories
SORT_DIRS = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".svg"],
    "Documents": [".pdf", ".docx", ".txt", ".md"],
    "Videos": [".mp4", ".mov", ".mkv"],
    "Archives": [".zip", ".rar", ".tar", ".gz"],
    "Executables": [".exe", ".msi", ".sh", ".bat"],
    "Code": [".py", ".js", ".html", ".css", ".cpp", ".java"],
    "Audio": [".mp3", ".wav", ".flac"],
    "Other": []
}

def move_file(file_path):
    ext = file_path.suffix.lower()
    target_folder = "Other"
    for folder, extensions in SORT_DIRS.items():
        if ext in extensions:
            target_folder = folder
            break
    destination = DOWNLOADS / target_folder
    destination.mkdir(exist_ok=True)
    shutil.move(str(file_path), str(destination / file_path.name))

def declutter_downloads():
    try:
        file_count = 0
        for item in DOWNLOADS.iterdir():
            if item.is_file():
                move_file(item)
                file_count += 1
        messagebox.showinfo("Success", f"Organized {file_count} files.")
    except Exception as e:
        messagebox.showerror("Error", str(e))

# GUI
root = Tk()
root.title("Declutter Downloads")
root.geometry("300x150")

Label(root, text="Declutter your Downloads folder!", pady=10).pack()
Button(root, text="Start Declutter", command=declutter_downloads, width=20).pack(pady=20)

root.mainloop()

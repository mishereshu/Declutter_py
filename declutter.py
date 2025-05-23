import os
import shutil
from pathlib import Path
from datetime import datetime
import platform

#Cross-platform Downloads folder detection
if platform.system() == "Windows":
    DOWNLOADS = Path(os.environ["USERPROFILE"]) / "Downloads"
else:
    DOWNLOADS = Path.home() / "Downloads"

#Subfolders to organize into
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

#Move file to the matching folder
def move_file(file_path):
    ext = file_path.suffix.lower()
    target_folder = None

    for folder, extensions in SORT_DIRS.items():
        if ext in extensions:
            target_folder = folder
            break
    if not target_folder:
        target_folder = "Other"

    destination = DOWNLOADS / target_folder
    destination.mkdir(exist_ok=True)

    try:
        shutil.move(str(file_path), str(destination / file_path.name))
        print(f"Moved: {file_path.name} → {target_folder}/")
    except Exception as e:
        print(f" Failed to move {file_path.name}: {e}")

#Scan and sort files
def decrapify():
    print(f"\n Cleaning up: {DOWNLOADS}")
    for item in DOWNLOADS.iterdir():
        if item.is_file():
            move_file(item)
    print("Done!")

if __name__ == "__main__":
    decrapify()

#declutter.py A Smart Downloads Folder Organizer

Tired of digging through a chaotic `~/Downloads` folder?

`declutter.py` is a Python utility that automatically organizes your Downloads directory by:

- 📁 File type (e.g. PDFs, Images, Archives)
- 📅 Date modified
- 📦 File size (large vs small)
- 📝 Optional logging for undoing changes

---

##Features

- Sorts files into clean subfolders like `/Downloads/Documents`, `/Downloads/Images`, etc.
- Automatically creates folders based on file type
- Moves large files into a separate folder (`/Downloads/Large Files`)
- Works cross-platform (Linux, macOS, Windows)

---

## 🔧 Installation

Make sure you have Python 3 installed.

```bash
git clone https://github.com/mishereshu/declutter.py.git
cd declutter.py

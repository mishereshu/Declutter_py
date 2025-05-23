# Declutter.py — Smart Downloads Folder Organizer

Are you tired of searching through a cluttered `~/Downloads` folder? `declutter.py` is a Python utility that automatically organizes your Downloads directory by sorting files based on:

* File type (e.g., PDFs, Images, Archives)
* Date modified
* File size (large vs. small)
* Optional logging for undoing changes

## Features

* Organizes files into well-structured subfolders like `/Downloads/Documents`, `/Downloads/Images`, etc.
* Automatically creates folders based on file type if they don’t exist.
* Moves large files to a dedicated folder (`/Downloads/Large_Files`).
* Cross-platform support: works on Linux, macOS, and Windows.

## Installation

Make sure you have Python 3 installed on your system.

```bash
git clone [https://github.com/mishereshu/declutter.py.git](https://github.com/mishereshu/declutter.py.git)
cd declutter.py

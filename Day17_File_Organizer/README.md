# Day 17 – File Organizer

This project is part of the 30 Days Python Challenge.

The File Organizer program automatically organizes files in a given directory by their file extensions.  
Each file is moved into a folder named after its extension, helping keep directories clean and structured.

## Features
- Reads all files from a specified folder
- Automatically creates folders based on file extensions
- Moves files into their corresponding extension folders
- Skips directories to avoid errors
- Handles empty or invalid paths safely

## Concepts Used
- Functions
- Loops
- Conditional statements
- Working with the file system
- Built-in Python libraries (`os`, `shutil`)

## How It Works
1. User enters a folder path
2. Program scans all files in the folder
3. Files are grouped by extension
4. New folders are created if needed
5. Files are moved into their respective folders

## How to Run
```bash
python file_organizer.py

# Day 28 — Screenshot Tool

This project is a simple **Screenshot Tool** built using Python as part of my **30-Day Python Challenge**.

The app takes a screenshot of the entire screen and saves it as a PNG file.

## Features
- Takes a screenshot after a 3-second delay
- Saves the screenshot automatically as `screenshot.png`
- Simple and beginner-friendly tool for capturing the screen

## How It Works
1. The program waits for 3 seconds before taking a screenshot.
2. The screenshot is captured using the **Pillow (PIL)** library.
3. The screenshot is saved as `screenshot.png` in the current directory.

## Requirements
- Python 3
- `Pillow` library (for image handling)
- Install Pillow using:

```bash
pip install pillow
```

## How to Run

```bash
python screenshot_tool.py
```

## Concepts Used

* Working with external libraries (Pillow)
* Time delay functionality
* File handling (saving images)
* Basic user input/output handling

## Author

Part of a 30-Day Python Challenge


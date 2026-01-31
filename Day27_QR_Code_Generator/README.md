# Day 27 — QR Code Generator (Website URL)

This project is a simple **QR Code Generator** built using Python as part of my **30-Day Python Challenge**.

The app generates a QR code for any valid website URL and saves it as a PNG file.

## Features
- Validates user input for website URLs
- Generates a QR code for any valid URL
- Saves the QR code as an image (`.png`)
- Allows generating multiple QR codes without restarting

## How It Works
1. The user enters a valid URL starting with `http://` or `https://`.
2. The program generates a QR code for the entered URL.
3. The QR code is saved as `website_qr.png` in the current directory.
4. The user can choose to generate another QR code or exit.

## Requirements
- Python 3
- `qrcode` library
- Install `qrcode` using:

```bash
pip install qrcode

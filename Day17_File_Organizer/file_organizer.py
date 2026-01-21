# 30-day Python challenge
print("------30-day Python challenge 17/30------")
print("File Organizer 📂")

import os
import shutil


def get_file_extension(filename):
    """Return the file extension without dot"""
    return filename.split(".")[-1].lower()


def create_folder(folder_name):
    """Create folder if it does not exist"""
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)


def organize_files(path):
    """Organize files in the given folder by extension"""

    if not os.path.exists(path):
        print("❌ Path does not exist.")
        return

    files = os.listdir(path)

    if not files:
        print("📭 Folder is empty.")
        return

    for file in files:
        file_path = os.path.join(path, file)

        # Skip folders
        if os.path.isdir(file_path):
            continue

        extension = get_file_extension(file)
        folder_name = extension.upper() + "_Files"

        create_folder(os.path.join(path, folder_name))

        shutil.move(
            file_path,
            os.path.join(path, folder_name, file)
        )

    print("✅ Files organized successfully!")


# -------- Main Program --------
folder_path = input("Enter folder path to organize: ").strip()
organize_files(folder_path)

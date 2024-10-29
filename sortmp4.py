import os
import shutil
import sys

def move_matching_files():
    # Here put your path of the source folder (where all the mp4 files are first downloaded)
    # replace C:\coding\test2 with the path of the folder where the mp4 files are first downloaded
    source_folder = r"C:\coding\test2"
    # Here put your path of the destination folder (where you want to move the mp4 files)
    # replace C:\coding\test2 with the path of the folder where you want to move the mp4 files
    destination_folder = r"C:\coding\test2"
    # Here put the strings you want to search for in the filename and match. Note that the strings will create a new folder AND look for files with that specfic string in the filename.
    strings = ["duck", "cat"]

    if not os.path.isdir(source_folder):
        print(f"The folder '{source_folder}' does not exist.")
        return

    # Loop through each file in the source folder
    for filename in os.listdir(source_folder):
        # Process only .mp4 files
        if filename.endswith(".mp4"):
            # Check if any of the strings are in the filename
            for string in strings:
                if string in filename:
                    # Create the destination folder if it doesn't exist
                    if not os.path.isdir(destination_folder):
                        os.makedirs(destination_folder, exist_ok=True)
                    destination_folder = os.path.join(source_folder, string)
                    os.makedirs(destination_folder, exist_ok=True)
                    
                    # Move the file to the destination folder
                    source_path = os.path.join(source_folder, filename)
                    destination_path = os.path.join(destination_folder, filename)
                    
                    shutil.move(source_path, destination_path)
                    print(f"Moved '{filename}' to '{destination_folder}'")
                    break  # Move on to the next file once a match is found

if __name__ == "__main__":
    # First argument is the source folder, remaining arguments are the strings to search fo
    move_matching_files()

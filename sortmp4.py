import os
import shutil
import sys

def move_matching_files(source_folder, destination_folder, *strings):
    # Ensure the source folder exists
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
                    
                    
                    # Move the file to the destination folder
                    source_path = os.path.join(source_folder, filename)
                    destination_path = os.path.join(destination_folder, filename)
                    
                    shutil.move(source_path, destination_path)
                    print(f"Moved '{filename}' to '{destination_folder}'")
                    break  # Move on to the next file once a match is found

if __name__ == "__main__":
    # First argument is the source folder, remaining arguments are the strings to search for
    if len(sys.argv) < 4:
        print("Usage: python move_files.py <source_folder> <destination_folder> <string1> <string2> ...")
    else:
        source_folder = sys.argv[1]
        destination_folder = sys.argv[2]
        strings = sys.argv[3:]
        move_matching_files(source_folder, destination_folder, *strings)

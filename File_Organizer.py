import os
import shutil

print("\n Getting Started: Welcome to the File Organizer! \n")

# Take the directory path as input
directory = input("Enter the directory path to organize: ")

# Define the categories and their corresponding extensions
categories = {
    'Scattered_Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.tif', '.webp', '.svg', '.ico', '.jfif'],
    'Scattered_PDFs': ['.pdf'],
    'Scattered_Audios':['.mp3', '.wav', '.aac', '.flac', '.wma', '.ogg', '.m4a', '.amr', '.mid', '.midi', '.ra', '.rm'],
    'Scattered_Videos': ['.ts','.3g2', '.3gp', '.avi', '.flv', '.h264', '.m4v', '.mkv', '.mov', '.mp4', '.mpeg', '.mpg', '.rm', '.swf', '.vob', '.wmv'],
    'Scattered_Files': ['.doc', '.docx', '.dot', '.dotx', '.docm', '.dotm', '.csv', '.xls', '.xlsx', '.xlsm', '.xlsb', '.ppt', '.pptx', '.pptm', '.pot', '.potx', '.potm', '.ppsx', '.ppsm', '.gdoc', '.gsheet', '.gslides', '.gdraw', '.gtable', '.gform', '.gscript', '.glink', '.gmap']
}

# Create the category folders if they don't exist
for category in categories:
    folder_path = os.path.join(directory, category)
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

# Loop through all files in the directory and move them to the corresponding category folder
for file_name in os.listdir(directory):
    file_path = os.path.join(directory, file_name)
    if os.path.isfile(file_path):
        file_extension = os.path.splitext(file_name)[1].lower()
        for category, extensions in categories.items():
            if file_extension in extensions:
                category_path = os.path.join(directory, category)
                new_file_path = os.path.join(category_path, file_name)
                i = 1
                while os.path.exists(new_file_path):
                    file_name_without_ext, ext = os.path.splitext(file_name)
                    new_file_name = f"{file_name_without_ext}_{i}{ext}"
                    new_file_path = os.path.join(category_path, new_file_name)
                    i += 1
                shutil.move(file_path, new_file_path)

# Delete any empty category folders
for category in categories:
    folder_path = os.path.join(directory, category)
    if os.path.exists(folder_path) and not os.listdir(folder_path):
        os.rmdir(folder_path)

print("\nFiles are Organized and Sorted by Name!!\n")

input("\n Press Enter to Close The Program!! \n")
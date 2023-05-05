# File Organizer

File Organizer is a simple yet powerful program that helps you organize your files based on their type and extension. With just a few clicks, you can easily sort your files into different categories, such as images, videos, audios, PDFs, and more. The program is available for both Windows and Linux operating systems.

## Windows Installation

To use the program on Windows, follow these steps:

1. Download the File Organizer program from the [link](https://github.com/MustakAbsarKhan/File_Organizer/raw/main/exe_file/File_Organizer.exe).
2. Double click the downloaded `File_Organizer.exe` file to launch the program.

## Linux Installation

Before using the script, make sure you have Python installed on your Linux machine. If not, you can install it by running the following command:

```bash
sudo apt-get update
sudo apt-get install python3
```

You also need to install the `shutil` module, which is used for moving and renaming files. You can install it using pip by running the following command:

```bash
pip3 install shutil
```

## Usage

### Windows

Once the program is launched on Windows, follow these steps to use it:

1. Enter the directory path that you want to organize.
2. The program will automatically create category folders if they do not exist already.
3. The program will then loop through all the files in the specified directory and move them to the corresponding category folder.
4. Any empty category folders will be deleted automatically.
5. Once the program finishes organizing your files, you will see a message indicating that your files are organized and sorted by name.

### Linux

To use the script on Linux, follow these steps:

1. Download the `File_Organizer.py` script from this repository and save it in a directory where you want to organize your files.
2. Open the terminal and navigate to the directory where you saved the script.
3. Run the following command to execute the script:

```bash
python3 File_Organizer.py
```

4. The script will prompt you to enter the directory path that you want to organize. Enter the path and press Enter.

```bash
Enter the directory path to organize:
```

5. The script will then organize the files in the directory based on their file type and extension.
6. After the script finishes running, you will see the organized files in separate folders based on their categories.

## Contributing

File Organizer is an open-source project, and we welcome contributions from anyone who is interested in making the digital world a more organized place. To contribute to the project, simply fork the repository, make your changes, and submit a pull request.

## License

File Organizer is licensed under the [MIT license](https://github.com/MustakAbsarKhan/File_Organizer/blob/main/LICENSE), which means you are free to use, modify, and distribute the program as long as you provide attribution to the original authors.

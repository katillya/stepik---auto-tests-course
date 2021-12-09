import os

# Getting path to the directory of the currently executed file
current_dir = os.path.abspath(os.path.dirname(__file__))

# Adding to the path the file name
file_path = os.path.join(current_dir, 'file.txt')

print("The file path is: ", file_path)

print(os.path.abspath(__file__))
print(os.path.abspath(os.path.dirname(__file__)))
import os
import shutil

# Set path to automation folder
path = r"{Directory Path to Automated Files}"

file_name = os.listdir(path)

# Find path
os.listdir(path)
# Created folder names
folder_names = ['Other', '{Parameter1Folder}', '{Parameter2Folder}', '{Parameter3Folder}', '{Parameter4Folder}', '{Parameter5Folder}']
folderNumber = len(folder_names)

# Check for existing paths
for loop in range(0, folderNumber):
    if not os.path.exists(path + folder_names[loop]):
        os.makedirs((path + folder_names[loop]))

for file in file_name:

    # Scrape and organize files based on parameters and move to folder name in array
    if "{Parameter1}" in file and not os.path.exists(path + folder_names[1] + "/" + file):
        shutil.move(path + file, path + folder_names[1] + "/" + file)

    elif "{Parameter2}" in file and not os.path.exists(path + folder_names[2] + "/" + file):
        shutil.move(path + file, path + folder_names[2] + "/" + file)

    elif "{Parameter3}" in file and not os.path.exists(path + folder_names[3] + "/" + file):
        shutil.move(path + file, path + folder_names[3] + "/" + file)

    elif "{Parameter4}" in file and not os.path.exists(path + folder_names[4] + "/" + file):
        shutil.move(path + file, path + folder_names[4] + "/" + file)

    elif ".{Parameter5}" in file and not os.path.exists(path + folder_names[5] + "/" + file):
        shutil.move(path + file, path + folder_names[5] + "/" + file)

    # Scrape for misc files by file type that don't meet above parameters, moves to base "Other" folder
    elif ".docx" in file and not os.path.exists(path + folder_names[0] + "/" + file):
        shutil.move(path + file, path + folder_names[0] + "/" + file)

    elif ".accdb" in file and not os.path.exists(path + folder_names[0] + "/" + file):
        shutil.move(path + file, path + folder_names[0] + "/" + file)

    elif ".txt" in file and not os.path.exists(path + folder_names[0] + "/" + file):
        shutil.move(path + file, path + folder_names[0] + "/" + file)

    elif ".xlsx" in file and not os.path.exists(path + folder_names[0] + "/" + file):
        shutil.move(path + file, path + folder_names[0] + "/" + file)

    elif ".xlsm" in file and not os.path.exists(path + folder_names[0] + "/" + file):
        shutil.move(path + file, path + folder_names[0] + "/" + file)

    elif ".pdf" in file and not os.path.exists(path + folder_names[0] + "/" + file):
        shutil.move(path + file, path + folder_names[0] + "/" + file)

    elif ".pptx" in file and not os.path.exists(path + folder_names[0] + "/" + file):
        shutil.move(path + file, path + folder_names[0] + "/" + file)

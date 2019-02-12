import os
import shutil
import re
from sys import platform

all_subject_regex = [] #User will input folder(subject) name, with that we will create Regex.
regex_pattern_and_corresponding_destination_folder  = {}

my_os = platform.lower()
if (my_os == 'windows') or (my_os == 'win32'):
    os_path_separator = '\\'
elif (my_os in 'linux'):
    os_path_separator = '/'

def createRegexAndAssociateDestinationPath(folder_name, folder_path):
    temp = folder_name.strip().lower().split()
    pattern = ("\s*".join(temp)) + ".*.pdf"
    all_subject_regex.append(pattern)
    regex_pattern_and_corresponding_destination_folder [pattern] = folder_path
    

def createFolder(total_folder, destination_parent_directory_path):
    print("\n\nAssumptions...")
    print("\n\t*Folder name must match with the subject's core name !")
    print("\tExample: If subject paper is Data Structure.pdf then enter folder name as Data Structure.")
    print("\tDo not write shortcuts as DS for Data Structure.\n")
    print("\t*Folder with same name must not exist.\n")
    print("\nEnter folder\'s name ...")
    os.chdir(destination_parent_directory_path)
    for i in range(total_folder):
        folder_name = input("{} : ".format(i + 1))
        os.mkdir(folder_name)

        folder_path = destination_parent_directory_path + "{}{}".format(os_path_separator, folder_name)

        createRegexAndAssociateDestinationPath(folder_name, folder_path)

def removeEmptyFolders(source_parent_directory_path):
    for dirs, subdir, files in os.walk(source_parent_directory_path):
        if(dirs == source_parent_directory_path):
            continue
        if not files:
            os.rmdir(dirs)      


def traverseAndMove(source_parent_directory_path):
    counter = 0 #Stores Total moved files
    print("\nMoving Files",end = " ")
    for dirs, subdir, file in os.walk(source_parent_directory_path):
        if (file):
            parent_folder = dirs
            year = dirs[-4:]#Extracting the year from yearwise folder name.

            for paper in file:#Traversing files in particular year in yearwise folder
                paper_path = parent_folder + "{}{}".format(os_path_separator, paper)#Required for shutil.move()
                
                for pattern in all_subject_regex:
                    if (re.match(pattern, paper.lower())):
                        
                        counter +=1
                        print(".",end = "")
                        

                        folder_path = regex_pattern_and_corresponding_destination_folder [pattern]
                        shutil.move(paper_path, folder_path)

                        #After moving file , renaming it to avoid "(Error:File already exis)"
                        file_in_destination = folder_path + "{}{}".format(os_path_separator, paper)
                        #To make filename unique, adding count(total file in the folder)
                        #between file_name and year.pdf.
                        other_name = file_in_destination[0:-4] + str(
                        len(next(os.walk(folder_path))[2])) +"  "+ year + file_in_destination[-4:]
                        os.rename(file_in_destination, other_name)
                        
    removeEmptyFolders(source_parent_directory_path)
    print("\nDone!\nTotal " + str(counter) + " files moved.")

def traverseAndMoveWhenSubjectFolderAlreadyExist(source_parent_directory_path, destination_parent_directory_path):
    for root, dirs, files in os.walk(destination_parent_directory_path):
        all_subject_folder_name_list = dirs
        break
    for subject_folder_name in all_subject_folder_name_list:
        folder_path = destination_parent_directory_path + "{}{}".format(os_path_separator, subject_folder_name)
        createRegexAndAssociateDestinationPath(subject_folder_name, folder_path)
    traverseAndMove(source_parent_directory_path)

if __name__ == '__main__':
    
    print("Question Papers are categorized  in year-wise manner.\
   \nOur aim is to categorize those papers in subject-wise manner.\n ")

    print("Key terms and their meaning...")
    print("\t*Source path = \"path of parent folder\" containing year-wise folders.\
\n\tExample =  D:\example\source    where source is parent folder of all year-wise folders\n")

    print("\t*Destination path = \"path of parent folder\" that will contain subject-wise folders.\
\n\tExample =  D:\example\destination \n\n")

    source_parent_directory_path = input("Enter Source path: ")
    destination_parent_directory_path = input("Enter Destination path: ")
    print('Select option...')
    print('\n1 : Subject Folder Already Exist.')
    print('2 : Create Subject Folder.')
    option = int(input('\nEnter your choice:: '))

    if(option == 1):
        traverseAndMoveWhenSubjectFolderAlreadyExist(source_parent_directory_path, destination_parent_directory_path)
    elif(option == 2):
        total_folder = int(input("Enter total number of subjects: "))
        createFolder(total_folder, destination_parent_directory_path)
        traverseAndMove(source_parent_directory_path)
    exitt = input("\nPress any key to exit!\n")

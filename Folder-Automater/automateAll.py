import os 
import shutil 

os.chdir('/home/nopc/Downloads/SCRAP DOWNLOAD')

def move_pdf():
    path_to_new_folder = f'{os.getcwd()}/PDFINHERE'
    for f in os.listdir():
        if f.endswith('.pdf'):
            current_file = f'{os.getcwd()}/{f}'
            shutil.move(current_file, path_to_new_folder)
            print("Success")

list_having_all_extensions = [] 
unique_extensions = []

def findall () :
    for f in os.listdir():
        ch = f.split('.')
        if len(ch) == 2:
            list_having_all_extensions.append(ch[1])
    removing_duplicates()    

def removing_duplicates ():
    unique_extensions = list(dict.fromkeys(list_having_all_extensions))
    print(unique_extensions)

def combining_all_pictures():
    new_folder_path = f'{os.getcwd()}/Photos'
    #os.mkdir(new_folder_path)
    for f in os.listdir():
        ch = f.split('.')
        if ch[-1] in ['jpeg', 'png', 'jpg', 'obj', 'JPEG']:
            current_file = f'{os.getcwd()}/{f}'
            shutil.move(current_file, new_folder_path)
            print("Success")

def combining_all_linux_and_windows_file():
    new_folder_path = f'{os.getcwd()}/Linux_And_Temp_Executable_Files'
    #os.mkdir(new_folder_path)
    for f in os.listdir():
        ch = f.split('.')
        if ch[-1] in ['bin', 'deb', 'exe', 'zip', 'rpm', 'gz', 'xz']:
            current_file = f'{os.getcwd()}/{f}'
            shutil.move(current_file, new_folder_path)
            print("Success")


def combining_all_ppts_and_doc():
    new_folder_path = f'{os.getcwd()}/PPTS_AND_DOCS'
    #os.mkdir(new_folder_path)
    for f in os.listdir():
        ch = f.split('.')
        if len(ch) == 2 and ch[1] in ['doc', 'odt', 'ppt', 'pptx']:
            current_file = f'{os.getcwd()}/{f}'
            shutil.move(current_file, new_folder_path)
            print("Success")


findall()
move_pdf()
combining_all_pictures()
combining_all_linux_and_windows_file()
combining_all_ppts_and_doc()
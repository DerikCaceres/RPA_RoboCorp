

import io
import json
import os
import shutil
import zipfile

def ReadJson(file):
    """Read json file and transform into dict"""
    content = io.open(file, mode="r", encoding="utf-8-sig").read()
    dict = json.loads(content)
    return dict
 

def Clear_Images_Folder(path):
    """Delete old images from the folder"""
    
    if os.path.exists(path):

        for filename in os.listdir(path):
            file_path = os.path.join(path, filename)

            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.remove(file_path)

            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)


def CreateFile(path, text):
    """Cria arquivo texto"""
    folder = os.path.dirname(path)
    if not os.path.exists(folder):
        os.makedirs(folder)

    f = open(path, "w", encoding='utf-8')
    f.write(text)
    f.close()



def zip_folder(folder_path, output_path):
    """Zip the contents of an entire folder (folder_path) and save it to output_path."""
    with zipfile.ZipFile(output_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(folder_path):
            for file in files:
                file_path = os.path.join(root, file)
                arcname = os.path.relpath(file_path, start=folder_path)
                zipf.write(file_path, arcname=arcname)




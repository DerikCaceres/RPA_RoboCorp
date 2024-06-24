

import io
import json
import os
import shutil


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
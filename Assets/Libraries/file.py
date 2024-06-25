

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
    """Delete the entire folder and its contents"""

    if os.path.exists(path) and os.path.isdir(path):
        shutil.rmtree(path)
        print(f"Folder '{path}' has been deleted.")
    else:
        print(f"Folder '{path}' does not exist.")


def Zip_Images(temp_dir, output_zip):
    """Create a zip file from the images in the temporary directory."""
    with zipfile.ZipFile(output_zip, 'w') as zipf:
        for root, _, files in os.walk(temp_dir):
            for file in files:
                file_path = os.path.join(root, file)
                zipf.write(file_path, os.path.relpath(file_path, temp_dir))

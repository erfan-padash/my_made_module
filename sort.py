import os
import re
import shutil


def show(path):
    direct = os.path.isdir(path)

    if not direct and path:
        raise ValueError('you send us a file not a directory or wrong path')
    com = re.compile(r'\.\w+')
    files_list = os.listdir(path)
    clean_files = {}

    for file in files_list:
        find = com.findall(file)
        if not len(find) == 0:
            if not find[-1] in clean_files.keys():
                clean_files[find[-1]] = [file]
            else:
                clean_files[find[-1]].extend([file])
    for key, value in clean_files.items():
        new_path = path + f'/all{key}'
        os.mkdir(new_path)
        for new_file in value:
            file_location = path + f'/{new_file}'
            shutil.move(file_location, new_path)



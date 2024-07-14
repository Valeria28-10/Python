# Задание №5
# Напишите функцию, которая ищет json файлы в указанной директории 
# и сохраняет их содержимое в виде одноименных pickle файлов.

import json
from pathlib import Path
import pickle

def json_to_pickle(path: Path) -> None:
    for obj in path.interdir():
        if obj.is_file() and obj.suffix == '.json':
            with(
                open (obj, 'r', encoding='UTF-8') as f_read:,
                open (obj.stem + ".pickle", 'wb') as f_write:
            ):
                data = json.load(f_read)
                pickle.dump(data, f_write)

if __name__== '__main__':
    json_to_pickle(Path(r'F:\PYTHON_COURSE'\Seminar_8'))
                    

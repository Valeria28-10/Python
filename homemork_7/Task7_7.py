# Задание №7

# Создайте функцию для сортировки файлов по директориям: видео, 
# изображения, текст и т.п.
# Каждая группа включает файлы с несколькими расширениями.
# В исходной папке должны остаться только те файлы, которые не 
# подошли для сортировки.

from pathlib import Path
import os
import shutil

def sort_files(path: str | Path, groups:dict[str:list[str]] = None) -> None:
    if not groups:
        groups = {
            Path("video"): ['avi', 'mov', 'mk4', 'mkv'],
            Path("images"): ['bmp', 'jpeg', 'jpg', 'png']
        }
    os.chdir(path)   
    reverse_groups = {}
    for target_dir, ext_list in groups.items():
        if not target_dir.is_dir():
            target_dir.mkdir()
    for ext in ext_list:
        reverse_groups[f'.{ext}'] = target_dir
    print(reverse_groups)   
    for file in path.interdir():
        if file.is_file() and file.suffix in reverse_groups:
            file.replace(reverse_groups[file.suffix] / file.name)

def gen_different_files(directory: str | Path, **kwarqs) -> None:
    if isinstance(directory, str):
        directory = Path(directory)
    if not directory.is_dir():
        directory.mkdir(parents=True)       
    os.chdir(directory)
    for ext, numbers in kwarqs.items():
        gen_different_files(ext, file_count=numbers)

if __name__== '__main__':
    gen_different_files(r"F:\PYTHON_COURSE\test", avi=2, 
                        doc=4, bin=3, jpg=5, mkv=6, png=3)
    sort_files(Path(r"F:\PYTHON_COURSE\test"))

 
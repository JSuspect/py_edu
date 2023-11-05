from pathlib import Path
import shutil

new_dir = Path.home() / 'my_folder'
new_dir.mkdir(exist_ok=True)

file_list = ['file1.txt', 'file2.txt', 'image1.jpg']

for files in file_list:
    paths = new_dir / files
    paths.touch()


img_move_dest = new_dir / 'images' / 'image1.jpg'
img_move_sour = new_dir / 'image1.jpg'

img_move_dest.parent.mkdir(exist_ok=True)
img_move_sour.replace(img_move_dest)

file1 = new_dir / 'file1.txt'

file1.unlink()
shutil.rmtree(new_dir)


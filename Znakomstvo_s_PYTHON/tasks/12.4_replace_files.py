import pathlib

home_dir = pathlib.Path.home()
work_dir = home_dir / 'Documents' / '_dev/wsl_dir/practice_files'
image_dir = work_dir / 'images'
doc_dir = work_dir / 'documents'
image_dir.mkdir(exist_ok=True)

for paths in doc_dir.glob('**/image*.??[gf]'):
    file_name = paths.name
    destination = image_dir / file_name
    paths.replace(destination)


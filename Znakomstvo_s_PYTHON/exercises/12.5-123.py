import pathlib

file_path = pathlib.Path.home() / 'slink/wsld' / 'test' / 'wrfiles/starships.txt'

file_path.parent.mkdir(parents=True, exist_ok=True)
file_path.touch()

list_words = ['Discowery', 'Enterprise', 'Defant', 'Voyager']

with file_path.open(mode='r+', encoding='utf-8') as file:
    for word in list_words:
        file.write(f'{word}\n')

file_open = file_path.open()
for i in file_open:
    print(i, end='')

print('----------------------------')

# Exercise 3
with file_path.open(mode="r", encoding="utf-8") as file:
    for starship in file.readlines():
        if starship.startswith("D"):
            print(starship, end="")

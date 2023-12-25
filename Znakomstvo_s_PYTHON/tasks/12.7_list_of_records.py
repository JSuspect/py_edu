import pathlib
import csv

file_path = pathlib.Path.home() / 'slink' / 'wsld' / 'practice_files' / 'scores.csv'

with file_path.open(mode='r', encoding='utf-8', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    scores = [row for row in reader]

high_scores = {}

for item in scores:
    name = item['name']
    score = int(item['score'])

    if name not in high_scores:
        high_scores[name] = score

    else:
        if score > high_scores[name]:
            high_scores[name] = score
    

output_csv_file = pathlib.Path.home() / 'slink' / 'wsld' / 'practice_files' / 'high_scores.csv'

with output_csv_file.open(mode='w', encoding='utf-8', newline='') as outfile:
    writer = csv.DictWriter(outfile, fieldnames=['name', 'high_score'])
    writer.writeheader()
    for name in high_scores:
        row_dict = {'name': name, 'high_score': high_scores[name]}
        writer.writerow(row_dict)
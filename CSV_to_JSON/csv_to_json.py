import csv
import json

file_name = input("Provide the CSV filename without extension>> ")

with open(f'{file_name}.csv') as f:

    reader = csv.reader(f, delimiter=',')

    titles = []
    temp_data = {}

    for heading in reader:
        titles = heading
        break

    for i, row in enumerate(reader, start=1):
        current_row = f"row{i}"
        temp_data[f'{current_row}'] = {}
        for col in range(len(titles)):
            temp_data[current_row][titles[col]] = row[col]
with open(f'{file_name}.json', 'w') as f_j:
    json.dump(temp_data, f_j, indent=4)

print("File converted successfully :)\n")